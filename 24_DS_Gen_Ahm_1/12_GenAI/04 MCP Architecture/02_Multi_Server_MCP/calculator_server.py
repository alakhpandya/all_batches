from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator Server")


@mcp.tool()
def add(a: int, b: int): 
    """Add two numbers"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int):
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def square(n: int):
    """Square a number"""
    return n * n


if __name__ == "__main__":
    mcp.run()

# This server has no idea about students.