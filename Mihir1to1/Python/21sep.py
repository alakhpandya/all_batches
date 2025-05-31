"""
f = open("trial.txt", "wt")
# content = input("Enter whatever you want to write in the file: ")
# f.write(content)
content_list = ["Today is Tuesday.\n", "It is raining outside.\n", "We will play TT if it is raining."]
f.writelines(content_list)
f.close()

# Append Mode
f = open("trial.txt", "a")
# print(f.readable())
f.write("\nWhen it becomes sunny, we will go for hiking.")
f.close()

# x mode
f = open("trial3.txt", "x")
print(f.readable())
print(f.writable())
f.close()

# r+ mode
f = open("trial.txt", "r+t")
f.write("Let's wait for Sunday.")
f.close()


# w+ mode
f = open("trial.txt", "w+t")
f.write("Let's wait for Sunday.")
f.close()

# a+ mode
f = open("trial.txt", "a+t")
# print(f.read())
f.write("Let's wait for Sunday.")
f.close()
"""