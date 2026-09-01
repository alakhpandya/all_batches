import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SQL Server")

connection = sqlite3.connect(
    "database.db",
    check_same_thread = False
)

cursor = connection.cursor()

# ------------------ Tool - 1 ------------------
@mcp.tool()
def list_tables() -> list:
    """Lists all the tables present in the database"""

    pass