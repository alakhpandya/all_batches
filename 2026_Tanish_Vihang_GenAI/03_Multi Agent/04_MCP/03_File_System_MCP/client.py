import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command= "python",
    args= ["file_server.py"]
)

async def main():

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # --------------------- List Tools ---------------------

            print("\n============== Tools ==============\n")
            tools = await session.list_tools()

            for tool in tools.tools:
                print(tool.name)

            # --------------------- Tool call ---------------------
            result = await session.call_tool(
                name= "list_files",
                arguments= {}
            )

            print("\n============== Files ==============\n")
            print(result)

            # --------------------- List Resources ---------------------

            print("\n============== Resources ==============\n")
            resources = await session.list_resources()

            for resource in resources:
                print(resource)

            # We don't see any resource here because we haven't called the "get_file_resource" function yet.

            print("\n============== Resource Template ==============\n")
            templates = await session.list_resource_templates()

            for template in templates.resourceTemplates:
                print(template)

            # Reading a resource
            resource_result = await session.read_resource(
                "workspace://files/ai_notes.txt"
            )

            print("\n============== Resource Result ==============\n")
            print(resource_result)



if __name__ == "__main__":
    asyncio.run(main())