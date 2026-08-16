from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Attendance Server")

@mcp.tool()
def dummy() -> None:
    """This is a dummy tool and does nothing"""

    return

if __name__ == "__main__":
    mcp.run()