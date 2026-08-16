from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name = "Calculator Server")


@mcp.tool()
def add(a: int, b: int, offset:int=0) -> int: 
    """Add two integers with an optional offset"""
    return a + b + offset


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers"""
    return a * b


@mcp.tool()
def square(n: int) -> int:
    """Squares a integer"""
    return n * n


if __name__ == "__main__":
    mcp.run()

# This server has no idea about students.