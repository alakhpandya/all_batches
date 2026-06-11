# agent.py
import asyncio
import os
import json
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 1. Initialize the official Google GenAI Client
# It automatically reads the GEMINI_API_KEY environment variable
gemini_client = genai.Client()

async def run_agent():
    # Define connection configuration to our local Python MCP Server
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )
    
    print("[Agent]: Initializing connection to MCP Server...")
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            
            # 2. Discover available tools from our MCP Server
            mcp_tools = await session.list_tools()
            all_tools = [mcp_tools.tools[i].name for i in range(len(mcp_tools.tools))]
            print(f"[Agent]: Successfully discovered tool: {all_tools}")
            
            # 3. Format MCP tools into Gemini Function Declaration Objects
            gemini_functions = []
            for tool in mcp_tools.tools:
                gemini_functions.append(
                    types.FunctionDeclaration(
                        name=tool.name,
                        description=tool.description,
                        parameters=tool.inputSchema  # Native JSON-Schema compatibility
                    )
                )
            
            # Pack declaration objects inside Gemini's explicit Tool configuration wrappers
            gemini_tools = [types.Tool(function_declarations=gemini_functions)]
            
            # 4. Define target interaction prompt
            # user_prompt = "I have 100 USD. How many Euros is that worth?"
            # user_prompt = "In the next prompt, I will provide how many bills of a certain currency are thre with me and will ask you the equivalent amount in another currency. Did you understand?"
            # user_prompt = "Explain what is crew.ai in simple language under 100 words."
            user_prompt = "It is 7:45 IST, what will be the current time in EST?"
            print(f"\n[User]: {user_prompt}")
            
            # We explicitly use gemini-2.5-flash as it is fast and supports function calling on the free tier
            model_id = "gemini-2.5-flash"
            
            # 5. Execute initial pass to Gemini providing our tool schemas
            response = gemini_client.models.generate_content(
                model=model_id,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    tools=gemini_tools,
                    temperature=0.0
                )
            )
            # print("Initial response from Gemini:", response.text)
            # print("Initial response from Gemini:", response)
            # print("Initial response from Gemini:", response.function_calls)
            
            # 6. Check if Gemini decided it needs to execute an external tool function
            if response.function_calls:
                # Initialize chat structure history for multi-turn reconciliation
                chat = gemini_client.chats.create(model=model_id)
                
                # Re-feed the prompt context to keep historical sync
                chat.send_message(user_prompt)
                
                for function_call in response.function_calls:
                    tool_name = function_call.name
                    # Gemini arguments arrive parsed natively as a dictionary
                    tool_args = function_call.args 
                    
                    print(f"[Agent]: Gemini triggered tool '{tool_name}' with args: {tool_args}")
                    print("[Agent]: Forwarding request execution to MCP Server...")
                    
                    # 7. Dynamically invoke execution block across stdio channel
                    mcp_result = await session.call_tool(tool_name, arguments=tool_args)
                    tool_output = mcp_result.content[0].text
                    print(f"[Server Response]: {tool_output}")
                    
                    # 8. Return structured function outcome object straight back to Gemini
                    final_response = chat.send_message(
                        types.Part.from_function_response(
                            name=tool_name,
                            response={"result": tool_output}
                        )
                    )
                
                print(f"\n[AI Agent Final Answer]: {final_response.text}")
            else:
                print(f"\n[AI Agent Response]: {response.text}")

if __name__ == "__main__":
    asyncio.run(run_agent())