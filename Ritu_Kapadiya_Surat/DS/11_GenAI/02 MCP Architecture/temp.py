fp = open("dependencies.txt", "r")
fp.read()
fp.close()

with open("dependencies.txt", "r") as fp:
    fp.read()

print("file pointer is automatically closed.")