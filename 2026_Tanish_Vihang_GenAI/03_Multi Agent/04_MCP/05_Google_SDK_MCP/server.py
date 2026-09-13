from mcp.server.fastmcp import FastMCP

# creating a server
mcp_server = FastMCP(name="Simple FastMCP server")


# def greet(name):
#     return f"Hello {name}! Welcome to the simple MCP server."

@mcp_server.tool()
def greet(name: str) -> str:
    """
    Greets the user
    """
    return f"Hello {name}! Welcome to the simple MCP server."


@mcp_server.tool()
def add_numbers(a: int, b: int, offset=0) -> int:
    """
    Adds two integers
    """
    return a + b + offset

# if __name__ == "__main__":
#     print("server.py file is running!")

if __name__ == "__main__":
    mcp_server.run()