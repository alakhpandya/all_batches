# Armstrong number program:
"""
l1 = []
myString = "Hello God!"
for ch in myString: # ch= 'H', 'e'....
    l1.append(ch)
print(l1)
"""
# n = int(input("n: "))

# ns = str(n)
# digits = []
# for digit in ns:
#     digits.append(digit**len(str(n)))

# powered_digits = [int(digit) ** len(str(n)) for digit in str(n)]

# if sum(powered_digits) == n:
#     print("Armstrong.")
# else:
#     print("Not Armstrong.")

# print("Armstrong.") if sum(powered_digits) == n else print("Not Armstrong.")


# n = int(input("n: "))
# print("Armstrong.") if sum([int(digit) ** len(str(n)) for digit in str(n)]) == n else print("Not Armstrong.")

a = int(input("First number: "))
b = int(input("Second number: "))
if a > b : a, b = b, a
for n in range(a, b+1):
    if sum([int(digit) ** len(str(n)) for digit in str(n)]) == n: print(n)
