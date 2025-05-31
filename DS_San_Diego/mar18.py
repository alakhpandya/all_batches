# commenting one line

# a = """
# commenting
# multiple lines
# """

# b = '''
# commenting
# multiple lines
# '''

# s1 = "my string"
# print(a)
# print(b)

# x = "Name: Alakh Pandya\nRole: Teacher"
# print(x)
# y = "
# Name: Rushabh Rupani
# Role: Student
# "
# z = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[31]

# # Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[32][33]

# # Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[35]"""
# print(z)


# print(f"""
# ------------------------Retail Invoice---------------------
# Customer Name: {name}
# Contact Number: {mobile}
# Date of Invoice: {date}
# -----------------------------------------------------------
# Items               Price       Quantity        Total
# item-1              50          3               150
# item-2              100         4               400
# item-3              40          5               200
#                                                 ---------
#                                 Final Amount:   750
# ----------------Thanks for shopping with us!---------------

# case 2- when customer is eligible for discount:

# ------------------------Retail Invoice---------------------
# Customer Name: xxxxxx
# Contact Number: xxxxxx
# Date of Invoice: 09-01-2022
# -----------------------------------------------------------
# Items               Price       Quantity        Total
# item-1              90          3               270
# item-2              100         4               400
# item-3              40          10              400
#                                                 ---------
#                                 Grand Total:    1070
#                                 Discount:        107
#                                                 ---------
#                                 Final Amount:    963
# ----------------Thanks for shopping with us!---------------
# """)

# -----------------------------------------------------------
# Items               Price       Quantity        Total
# item-1              50          3               150

# p1 = 50
# q1 = 3
# t1 = p1*q1
# p2 = 100
# q2 = 4
# t2 = p2*q2
# p3 = 40
# q3 = 10
# t3 = p3*q3
# print("-"*50)
# print("Items\tPrice\tQuantity\tTotal".expandtabs(12))
# print(f"Item-1\t{p1}\t{q1}\t{t1}".expandtabs(12))
# print(f"Item-2\t{p2}\t{q2}\t{t2}".expandtabs(12))
# print(f"Item-3\t{p3}\t{q3}\t{t3}".expandtabs(12))

# n = input("Enter number of items: ")
price = []
quantity = []
total = []
# for sr in range(1, n+1):
i = 1
while True:
    print(f"Item-{i}:")
    price.append(float(input("price: ")))
    quantity.append(float(input("quantity: ")))
    i += 1
    check = input("Press 'x' to exit or any other key to continue...").lower()
    if check == "x":
        break
