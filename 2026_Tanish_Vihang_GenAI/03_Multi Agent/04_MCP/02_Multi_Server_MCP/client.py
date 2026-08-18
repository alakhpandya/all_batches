import asyncio
from mcp import StdioServerParameters
from mcp import ClientSessionGroup


attend_server = StdioServerParameters(
    command= "python",
    args= ["attendance_server.py"]
)

calc_server = StdioServerParameters(
    command= "python",
    args= ["calculator_server.py"]
)

student_server = StdioServerParameters(
    command= "python",
    args= ["student_server.py"]
)

async def main():

    async with ClientSessionGroup() as group:
        # same as: group = ClientSessionGroup()

        await group.connect_to_server(attend_server)
        await group.connect_to_server(calc_server)
        await group.connect_to_server(student_server)

        """
        The SDK handles all:
        - launching the processes (stdio_client, read_stream, write_stream)
        - opening sessions (ClientSession)
        - initializing them (session.initialize())
        - tracking them
        """

        print("\nAavailable Tools:")

        print(group.tools)


if __name__ == "__main__":
    asyncio.run(main())