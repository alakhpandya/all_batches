# Remaining Topics: File Handling, Exception Handling & Resource management

# File Handling:
f = open("batch.txt")
# data = f.read()
# print(data)
"""
print(f.read(20))
print(f.read(30))

print("cursor's current position:", f.tell())
f.seek(28)
print(f.read())

print(f.readable())
print(f.readline())
print(f.readline())
f.seek(80)
print(f.readline())
"""
content = f.readlines()
print(content)
print(content[6])
# print(f.read())
print(f.closed)

f.close()
print(f.closed)

# Tomorrow's session: Modes, more about file handling