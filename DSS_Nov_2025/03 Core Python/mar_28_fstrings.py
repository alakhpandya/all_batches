# Take 5 integer inputs from the user & print the answer exactly as below:
"""
Sample inputs:
a = 1
b = 2
c = 3
d = 4
e = 5

Sample output:
The average of 1, 2, 3, 4 & 5 is: 3.0
"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
e = int(input("e = "))
avg = (a + b + c + d + e)/5
'''
print("The average of", a, end="")
print(",", b, end="")
print(",", c, end="")
print(",", d, "&", e, "is:", avg)
'''
print(f"The average of {a}, {b}, {c}, {d} & {e} is: {avg}")