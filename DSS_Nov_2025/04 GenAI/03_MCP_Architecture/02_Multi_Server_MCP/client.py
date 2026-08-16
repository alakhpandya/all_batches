import asyncio

from mcp import StdioServerParameters
from mcp.client.session_group import ClientSessionGroup     # Note that we are not importing ClientSession


calculator_server = StdioServerParameters(
    command="python",
    args=["calculator_server.py"]
)

student_server = StdioServerParameters(
    command="python",
    args=["student_server.py"]
)

attendance_server = StdioServerParameters(
    command="python",
    args=["attendance_server.py"]
)

async def main():

    async with ClientSessionGroup() as group:           # Think this as a "connection manager"
        # as good as writing: group = ClientSessionGroup()

        await group.connect_to_server(calculator_server)
        await group.connect_to_server(student_server)
        await group.connect_to_server(attendance_server)

        """
        The SDK handles all:
        - launching the processes
        - opening sessions
        - initializing them
        - tracking them
        """

        print("\nAvailable Tools:\n")

        for tool_name in group.tools:

            print(tool_name)

        # In a real-world application, here an LLM will decide which tool tobe called based on the user prompt

        result = await group.call_tool(

            "add",

            {
                "a": 100,
                "b": 250
            }

        )

        print("\nCalculator Result:")

        print(result)

        result = await group.call_tool(         

            "get_student_name",

            {
                "student_id": 103
            }

        )

        print("\nStudent Result:")

        print(result)


asyncio.run(main())