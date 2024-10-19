# Ways to take inputs:
"""
print("Enter a number:")
a = int(input())
b = int(input("Enter second number: "))
# print(a)
print("a =", a)
print("b =", b)
# c = a + b
# print("a + b =", int(a)+float(b))
print("a + b =", a + b)
print("type of a :", type(a))
print("type of b :", type(b))
"""
"""
Take 5 integers from user and store them into variables named a, b, c, d and e.
Calculate their average and print the final answer exactly like this:
Sample:
a = 2
b = 3
c = 4
d = 5
e = 6
Output should be:
Average of 2, 3, 4, 5 & 6 is: 4.0
"""
# f-string
"""
print("Enter 5 integers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
avg = (a + b + c + d + e)/5
print(f"Average of {a}, {b}, {c}, {d} & {e} is: {avg}")
"""
# Numeric data types:
# int
"""
a = 91837567481938138746187459192873261875127236912875129873214786578132698173456471832465469187348732647865817946832976518732469832746187568129374613546198273461875647819834136947861237851648793786
print(type(a))
"""
# float
"""
b = 9284372638470143756208475602347945798032489572035698.347259874398072093875928769027834907259807593408
print(type(b))
c = 5
"""
# complex
'''
d = 5 + 6j
print(d)
print(type(d))
'''

# Collections:
# strings: Ordered and Immutable collection of characters
"""
a = "c"
b = 'a random string.'
print(a + b)
# print(a - b)
# print(a / b)
print(b * 3)

s2 = "and"
s3 = "dna"
"""
s1 =        "Today is Thursday and it looks like it will not rain, but forecast says that it will be a light rain."
# index nos: 0123456789
print(s1)
print(len(s1))
print(s1[50])
s2 = s1[5 : 10]
print(s1)
print(s2)
print(s1[20 : 90])
# print(s1[500])
# print(s1[20 : 500])
print(s1[20 : ])
print(s1[ : 20])
print(s1[ : ])

print(s1[20 : 20])
print(s1[6 : 100 : 2])
