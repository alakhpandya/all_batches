myString = "Mihir Shah is the next tech-star from India"
print(myString.partition("next"))
print(myString.rpartition("next"))
# lst = myString.split()
# print(lst)
str1 = "I love Python. I love Royal."
print(str1.partition("love"))
print(str1.rpartition("love"))
print(myString.removeprefix("Mihir "))
print(myString.removesuffix("India"))

print(myString.replace("i", "k", 2))
# myString = (myString.replace("India", "US"))

print(myString.rfind("h"))
print(myString.rindex("h"))

date = input("Enter date (dd): ")
month = input("Enter month (mm): ")
year = 2021
# print("Date:", date.zfill(2), "/", month.zfill(2), "/", year)
print(f"Date: {date.zfill(2)}/{month.zfill(2)}/{year}")