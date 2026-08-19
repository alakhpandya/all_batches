import asyncio
from mcp import StdioServerParameters
from mcp import ClientSessionGroup
from pprint import pprint
import json

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

        # pprint(group.tools)

        for tool_name in group.tools:
            print(tool_name)

        # In a real-world application, here an LLM will decide which tool tobe called based on the user prompt

        result = await group.call_tool(
            name = "add", 

            arguments = {
                "a" : 15,
                "b" : 25
            }
        )

        print("\nResult of 'add' from calculator server:")
        print(result)

        result = await group.call_tool(
            name = "get_student_info",

            arguments = {
                "student_id" : 102
            }
        )

        print("\nResult of 'get_student_info' from student server:")
        result = json.loads(result.content[0].text)
        pprint(result)


if __name__ == "__main__":
    asyncio.run(main())


"""
Why is this amazing?
Imagine tomorrow if we add:

Email Server,

PDF Server,

Weather Server,

Finance Server etc.

then will we re-write our client.py?

No, we will simply connect more servers and the architecture will scale-up naturally.
"""

"""
Fun question: What happens if two servers both have a tool named add()?
"""

# Task: Convert this code into the one that calls an LLM.