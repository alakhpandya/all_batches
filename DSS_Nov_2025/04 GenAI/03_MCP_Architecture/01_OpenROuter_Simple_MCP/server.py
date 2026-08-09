# pip install mcp
from mcp.server.fastmcp import FastMCP

# Creating MCP Server
mcp_server = FastMCP(name= "Basic MCP Server")

@mcp_server.tool()
def greet(name: str) -> str:
    """
    Greets the user.
    """
    return f"Hello {name}, Welcome to MCP!"


@mcp_server.tool()
def add_numbers(a: int, b:int, offset=0) -> int:
    """
    Adds two numbers.
    """
    return a + b + offset

if __name__ == "__main__":
    mcp_server.run()