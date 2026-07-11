from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="dummy_server")

@mcp.tool()
def dummy():
    """Does nothing"""
    return "This is a dummy tool"


if __name__ == "__main__":
    mcp.run()