from pprint import pprint
import sqlite3

connection = sqlite3.connect(
    "database.db",
    check_same_thread=False
)
cursor = connection.cursor()

# sql = 'select * from customers where city="Ahmedabad"'
sql = 'select * from customers;'
sql_lower = sql.strip().lower()

cursor.execute(sql)
rows = cursor.fetchall()

print("\nDescription:")
pprint(cursor.description)

column_names = [

    row[0]

    for row in cursor.description

]
print("\nColumn Names:\n", column_names, "\n")

results = []

for row in rows:

    results.append(

        dict(zip(column_names,row))

    )

print("\nResult:") 
pprint(results)