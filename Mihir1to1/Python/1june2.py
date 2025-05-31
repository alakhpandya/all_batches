# sets: unordered & mutable collection of elements in which repeatition is eliminated
"""
ordered & mutable: list
ordered & immutable: tuple
unordered & mutable: set
"""
s1 = {"Mihir", "Armaan", "Akshayraj", "Yash", "Mihir", "Mihir"}
print(s1)       # sets are unordered!
print(type(s1))
print(len(s1))
# print(s1[2])  # index numbers do not exist
s1.add("Mihir") 
print(s1)       # repeatition eliminated
print(min(s1))
print(max(s1))
print(sorted(s1))   # sorted always returns you a list
list2 = [1, 2, 3, 4]
s2 = set(list2)
tup3 = [3, 4, 5, 6]
s3 = set(tup3)
s4 = {5, 6, 7, 8}
l4 = list(s4)
t4 = tuple(s4)
print(s2)
print(s3)
print(s4)
print(l4)
print(t4)
str5 = "Mihir"
l5 = list(str5)
t5 = tuple(str5)
print(l5)
print(t5)
s5 = set("Mihir")
print(s5)
l6 = [1, "Mihir", ["Python", "C++"], ("Alakhsir", "Rahulsir"), {"SQL", "Madhusudansir"}]
print(l6)   # You can nest anything in a list & in a tuple
s7 = {1, "Mihir", ("Python", "C++")}
# s8 = {1, "Python", {1,2,3}, [5,6,7]}  Only immutables can become members of sets (ie. strings, numbers & tuples)
print(s7)
# set methods: regular methods & set operation methods