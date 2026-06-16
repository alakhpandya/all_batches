from google import genai
from mcp import StdioServerParameters, ClientSession
import asyncio
from mcp.client.stdio import stdio_client
from google.genai import types

# 1. Initialize the official Google GenAI Client
# It automatically reads the GEMINI_API_KEY environment variable
print("[Agent]: Connecting to the Gemini server...")
gemini_client = genai.Client()
# gemini_client = genai.Client(api_key="Your API key")

async def run_agent():
    # Define connection configuration to our local Python MCP Server
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    print("[Agent]: Initializing the connection to the MCP server...")
    async with stdio_client(server_params) as (read_stream, write_stream):
        # (read_stream, write_stream) = stdio_client(server_params)
        async with ClientSession(read_stream, write_stream) as session:
            # session = ClientSession(read_stream, write_stream)
            await session.initialize()

            # 2. Find out available tools on our MCP server
            mcp_tools = await session.list_tools()
            # print(mcp_tools)
            all_tools = [mcp_tools.tools[i].name for i in range(len(mcp_tools.tools))]
            # print(all_tools)
            print("[Agent]: Successfully discovered these tools:", all_tools)

            # 3. Format the MCP Tools into Gemini's Function Declaration Object
            # types.FunctionDeclaration(
            #     name=mcp_tools.tools[0].name,
            #     description=mcp_tools.tools[0].description,
            #     parameters=mcp_tools.tools[0].inputSchema
            # ) 
            gemini_functions = []
            for tool in mcp_tools.tools:
                gemini_functions.append(types.FunctionDeclaration(
                        name=tool.name,
                        description=tool.description,
                        parameters=tool.inputSchema
                    )
                ) 
            
            # Pack declaration objects inside Gemini's explicit Tool configuration wrapper
            gemini_tools = [types.Tool(function_declarations=gemini_functions)]

            # 4. Taking the prompt from the user
            user_prompt = "I have 200 USD. How many Euros is that worth?"
            # user_prompt = "I am a student who is learning GenAI, can you give me a suggestion in under 30 words?""
            
            print(f"\n[User]: {user_prompt}")

            # We explicitly use gemini-2.5-flash as it is fast and supports function calling on the free tier
            model_id = "gemini-2.5-flash"
            
            # 5. Execute initial pass to Gemini providing our tool schemas
            response = gemini_client.models.generate_content(
                model=model_id,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    tools = gemini_tools,
                    temperature = 0.0
                )
            )
            # print(response)
            # print("Resonse from Gemini:", response.text)
            # print("Resonse from Gemini:", response.function_calls)

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

                    print(f"[Agent]: Gemini has identified the {tool_name} tool to call with arguments ={tool_args}")
                    print("[Agent]: Forwarding request execution to MCP Server...")

                    # 7. Dynamically invoke execution block across stdio channel
                    mcp_result = await session.call_tool(tool_name, arguments=tool_args)
                    # print(mcp_result)
                    tool_output = mcp_result.content[0].text
                    print(f"[Server]: {tool_output}")

                    # print(f"""
                    #     {types.Part.from_function_response(
                    #     name= tool_name,
                    #     response= {"result" : tool_output}
                    # )}
                    # """)
                    final_response = chat.send_message(
                        types.Part.from_function_response(
                            name= tool_name,
                            response= {"result" : tool_output}
                        )
                    )
                    print("[Agent]:", final_response.text)

            else:
                print(f"[Agent]: {response.text}")

if __name__ == "__main__":
    asyncio.run(run_agent())