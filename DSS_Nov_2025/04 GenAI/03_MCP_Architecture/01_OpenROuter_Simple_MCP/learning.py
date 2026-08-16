"""
f = open("demo.txt", "r")

text = f.read()

f.close()

print(text)
"""

with open("demo.txt", "r") as f:
    text = f.read()


print(text)

# this = that     =>  with that as this: