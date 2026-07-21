import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SQL Server")

connection = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = connection.cursor()


@mcp.tool()
def list_tables():

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    rows = cursor.fetchall()

    return [row[0] for row in rows]


@mcp.tool()
def describe_table(table_name: str):

    cursor.execute(f"PRAGMA table_info({table_name})")

    rows = cursor.fetchall()

    columns = []

    for row in rows:

        columns.append({

            "column": row[1],

            "type": row[2]

        })

    return columns


@mcp.tool()
def execute_query(sql: str):

    sql_lower = sql.strip().lower()

    if not sql_lower.startswith("select"):

        return {

            "status":"error",

            "message":"Only SELECT queries are allowed."

        }

    try:

        cursor.execute(sql)

        rows = cursor.fetchall()

        column_names = [

            description[0]

            for description in cursor.description

        ]

        results = []

        for row in rows:

            results.append(

                dict(zip(column_names,row))

            )

        return results

    except Exception as e:

        return {

            "status":"error",

            "message":str(e)

        }


if __name__ == "__main__":

    mcp.run()