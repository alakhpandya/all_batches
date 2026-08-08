my_list = ["apple", "mango", "banana", "strawberries"]

print(list(enumerate(my_list)))

for index, fruit in enumerate(my_list):
    print(f"{index}\t{fruit}")


fruits = ["apple", "mango", "banana", "strawberries"]

# apple-mango-banana-strawberries
"-".join(fruits)