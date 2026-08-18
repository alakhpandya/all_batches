from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name = "Calculator Server")

@mcp.tool()
def dummy() -> None:
    """This is a dummy method and does nothing"""
    return


if __name__ == "__main__":
    mcp.run()