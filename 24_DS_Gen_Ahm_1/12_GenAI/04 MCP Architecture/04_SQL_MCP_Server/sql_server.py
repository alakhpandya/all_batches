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

# sqlite_master: Think it as an invisible table created by sqlite to keep all the data (metadata) of the database handy. Example:
"""
type        name            sql
table       customers       create table customers...
table       products        create table products...
table       orders          create table orders...
index       ...             ...
view        ...             ...
view        ...             ...
trigger     ...             ...
"""

# cursor.fetchall(): Converts & returns all the rows of the result table in form of a list of tuples. Example:
# if our query is: "select * from customers" then cursor.fetchall() will return:
"""
[
    (1,"Alice","Ahmedabad"),
    (2,"Bob","Surat"),
    (3,"Charlie","Rajkot"),
    (4,"David","Ahmedabad")
]
"""
# similar methods: cursor.fetchone() - fetches only the first row; cursor.fetchmany(15) - fetches first 15 rows.

@mcp.tool()
def describe_table(table_name: str):

    cursor.execute(f"PRAGMA table_info({table_name})")          # PRAGMA of sqlite = DESCRIBE of mySQL => "DESCRIBE table {table_name}"

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