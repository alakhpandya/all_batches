# Resource Management - with statement
# file = open("GoogleStockData.csv", "a+")
"""
with open("GoogleStockData.csv", "a+") as file:
    file.seek(0)
    for row in file:
        print(row)
        break
    print(file.closed)
print(file.closed)
print("Thanks")
"""

# with statement and OOP

class ContextManager():
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print(exc_type)
        print(exc_value)
        print(traceback)

file_path = input("Enter file name with full path and extension: ")
mode = input("Enter opening mode: ")
# f = ContextManager(file_path, mode)
# print(f.file_path)
# print(f.mode)
with ContextManager(file_path, mode) as f:
    # print(f.file_path)
    # print(f.mode)
    print(f.read())
    print(f.closed)
print(f.closed)
