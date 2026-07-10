from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("My First MCP Server")


@mcp.tool()
def greet(name: str) -> str:
    """
    Greets the user.
    """
    return f"Hello {name}! Welcome to MCP."


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers.
    """
    return a + b


if __name__ == "__main__":
    mcp.run()