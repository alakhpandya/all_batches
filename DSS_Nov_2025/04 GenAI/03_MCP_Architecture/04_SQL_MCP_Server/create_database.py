import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

# customer table
cursor.execute("""
    CREATE TABLE customers(
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        city TEXT
    )
""")

# product table
cursor.execute("""
    CREATE TABLE products(
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL
    )
""")

# orders table
cursor.execute("""
    CREATE TABLE orders(
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        order_date TEXT
    )
""")

# inserting data into customer table
customers = [
    (1,"Alice","Ahmedabad"),
    (2,"Bob","Surat"),
    (3,"Charlie","Rajkot"),
    (4,"David","Ahmedabad")
]

cursor.executemany(
    "INSERT INTO customers VALUES(?, ?, ?)",
    customers
)

# inserting data into products table
products = [
    (1,"Laptop",65000),
    (2,"Mouse",800),
    (3,"Keyboard",1500),
    (4,"Monitor",18000)
]

cursor.executemany(
    "INSERT INTO products VALUES(?,?,?)",
    products
)

# inserting data into orders table
orders = [
    (1,1,1,1,"2026-01-01"),
    (2,1,2,2,"2026-01-02"),
    (3,2,4,1,"2026-01-03"),
    (4,3,3,3,"2026-01-04"),
    (5,4,1,2,"2026-01-05")
]

cursor.executemany(
    "INSERT INTO orders VALUES(?,?,?,?,?)",
    orders
)

connection.commit()

connection.close()

print("Database created successfully!")