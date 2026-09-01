import sqlite3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SQL Server")

connection = sqlite3.connect(
    database= "database.db",
    check_same_thread= False
)
cursor = connection.cursor()

# --------------------------- Tool-1 ---------------------------

@mcp.tool()
def list_tables() -> list:
    """Returns list of all the tables present in the database"""

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    rows = cursor.fetchall()
    # print(rows)

    result = []
    for tup in rows:
        result.append(tup[0])

    return result

# sqlite_master: is a invisible table created by sqlite itself to store and keep the metadata of the database (all the information about the database) handy. 
# Example:
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
# More about `cursor.fetchall()`:It converts & returns all the rows of the result table in form of a list of tuples. Example:
# if our query is: "select * from customers" then cursor.fetchall() will return:
"""
[
    (1,"Alice","Ahmedabad"),
    (2,"Bob","Surat"),
    (3,"Charlie","Rajkot"),
    (4,"David","Ahmedabad")
]
"""
# similar methods: 
# cursor.fetchone() - fetches only the first row; 
# cursor.fetchmany(15) - fetches first 15 rows.

# result = list_tables()
# print(result)

# --------------------------- Tool-2 ---------------------------

@mcp.tool()
def describe_table(table_name: str) -> list[dict]:
    """Provides the names of the columns and their datatypes"""

    cursor.execute(f"PRAGMA table_info({table_name})")      # PRAGMA in sqlite3 is same as DESCRIBE in mySql.
    # In mySql, we would write this query as - f"DESCRIBE table {table_name}""

    rows = cursor.fetchall()

    # print(rows)

    columns = []

    for row in rows:

        columns.append({

            "column" : row[1],

            "datatype" : row[2]

        })

    return columns


# print(describe_table("customers"))

# --------------------------- Tool-3 ---------------------------

@mcp.tool()
def execute_query(sql: str):
    """Executes the query provided in the argument on the database"""

    sql_lower = sql.lower()

    if not sql_lower.startswith("select"):

        return {

            "status" : "error",

            # "message" : "Only SELECT queries are allowed"
            "message" : "The database is READ ONLY"

        }

    try:

        cursor.execute(sql)

        rows = cursor.fetchall()

        # print(cursor.description)

        column_names = []
        for description in cursor.description:
            column_names.append(description[0])

        results = []

        for row in rows:

            results.append(

                # row
                dict(zip(column_names, row))

            )

        # print(results)

        return results


    except Exception as e:

        return {

            "status" : "error",

            "message" : str(e)

        }

# execute_query("SELECT * FROM customers;")

if __name__ == "__main__":

    mcp.run()