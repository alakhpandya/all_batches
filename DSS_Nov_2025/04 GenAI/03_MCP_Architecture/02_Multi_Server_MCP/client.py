import asyncio
from mcp import StdioServerParameters
from mcp.client.session_group import ClientSessionGroup

# calculator_server_path = "\\02_Multi_Server_MCP\\calculator_server.py"
# student_server_path = "\\02_Multi_Server_MCP\\student_server.py"
# attendance_server_path = "\\02_Multi_Server_MCP\\attendance_server.py"

# calculator_server_path = "calculator_server.py"
# student_server_path = "student_server.py"
# attendance_server_path = "attendance_server.py"

calculator_server = StdioServerParameters(
    command= "python",
    args=["calculator_server.py"]
)

attendance_server = StdioServerParameters(
    command= "python",
    args=["attendance_server.py"]
)

student_server = StdioServerParameters(
    command= "python",
    arg=["student_server.py"]
)

async def main():

    # group = ClientSessionGroup()
    async with ClientSessionGroup() as group:           # Think this as a "connection manager"

        await group.connect_to_server(calculator_server)
        await group.connect_to_server(attendance_server)
        await group.connect_to_server(student_server)

        """
        All these things are automatically handled by SDK:
        1. launching the entire process (read_stream, write_stream)
        2. opening a session
        3. initializing the session(s) (session.initialize())
        4. tracking all the sessions
        """

        print("\nAvailable Tools:\n")

        for tool_name in group.tools:
            print(tool_name)

        # In a real-world scenario, an LLM will decide which tool is to be called here

        result = await group.call_tool(
            name = "add",

            arguments = {
                "a" : 10,
                "b" : 40,
                "offset" : 50
            }

        )

        print("Calculator server output:", result)

        result = await group.call_tool(
            name = "get_student_name",

            arguments= {
                "student_id" : 101
            }
        )

        print("Student server output:", result)

if __name__ == "__main__":
    asyncio.run(main())