from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name = "Calculator Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two integers"""

    return a + b


@mcp.tool()
def multiply(a: int, b:int) -> int:
    "Multiplies two integers"

    return a * b


@mcp.tool()
def power(base: int, pow: int) -> float:
    """Returns the power of the base that is: base ^ pow"""

    return base ** pow


if __name__ == "__main__":
    mcp.run()