# Functions
def average(a, b):
    # print("This function was supposed to calculate average of two numbers...")
    # print("a =", a)
    # print("b =", b)
    # print(f"Average of {a} & {b} is: {(a + b)/2}")
    # return (a + b)/2
    c = (a + b)/2
    # print(f"Average of {a} & {b} is: {c}")
    return c


# x = int(input("x: "))   # 30
# y = int(input("y: "))   # 40
# average(10, 20)
# average(50, 100)
# average(x, y)

# a = int(input("a: "))   # 30
# b = int(input("b: "))   # 40
# average(a, b)

# x = int(input("x: "))   # 30
# y = int(input("y: "))   # 40
# average(x, y)

# Try to use above function to do this task:
"""
Ask four integers from user and print the sum of average of first two and average of last two calling it "final answer".
"""
"""
print("Enter four integers:")
p = int(input())
q = int(input())
r = int(input())
s = int(input())
final_answer = average(p, q) + average(r, s)
print("final answer =", final_answer)
"""

# Create a function 'average_of_3' that prints average of 3 numbers. Write a main program that asks 3 numbers from user and print their average using that function.

def sum_of_squares(a, b):
    print("sum of squares =", (a ** 2) + (b ** 2))

a = int(input("a: "))
b = int(input("b: "))

sum_of_squares(a, b)


"""
Create a function that returns sum of squares of two numbers given in its argument. Write a main program that takes four numbers from user & print division of sum of squares of first two numbers by sum of squares of last two numbers using the created function.
"""