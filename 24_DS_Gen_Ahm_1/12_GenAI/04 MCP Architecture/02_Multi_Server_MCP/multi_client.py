"""
Earlier our client connected using:
```
server_params = StdioServerParameters(
    command="python",
    args=["server.py"]
)
```
Because there was just one server, but now we have multiple servers. So which server should our agent connect to? Both?
Should we create two sessions? How will it manage two sessions?
For exampe, what if user asked: "How many students are there, and what is 25 x 18?"

Solution: `ClientSessionGroup`
It's job is to:
- Connect to multiple servers
- Discover tools from all servers
- Route tool calls to the correct server automatically
- Present one unified tool catalog to your application
"""

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

            "get_student",

            {
                "student_id": 103
            }

        )

        print("\nStudent Result:")

        print(result)


asyncio.run(main())

"""
Why is this amazing?
Imagine tomorrow if we add:

Email Server,

PDF Server,

Weather Server,

Finance Server,

Attendance Server etc.

then will we re-write our multi_client.py?

No, we will simply connect more servers and the architecture will scale-up naturally.
"""

"""
Fun question: What happens if two servers both have a tool named add()?
"""

# Task: Convert this code into the one that calls an LLM.