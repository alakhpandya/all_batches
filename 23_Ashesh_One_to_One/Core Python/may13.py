"""
numbers = [11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11]
print(numbers[5])
numbers[5] = 90         # item assignment
print(numbers)

vegetables = ["1tomato", "potato", "cabbage", "spinach", "Onion", "Lady finger", "", "cucumber", "Lemon"]
print(vegetables)
print(min(vegetables))
print(max(vegetables))
print(sorted(vegetables))

veg = "lady_finger"
print(min(veg))
print(max(veg))
print(sorted(veg))

mix_veg = ["tomato", "3", "potato", "1", "cabbage", "0.750", "spinach", "-0.5", "onion", "2"]
print(mix_veg)
print(type(mix_veg))
print(sorted(mix_veg))
"""
# Methods on lists: Methods of list can change the original list - lists are mutable
numbers = [11, 22, 33, 44, 11, 9, 13, 11, -56, 7.56, -15.87, 11, 37, 11]
print(numbers.append(1000))       # because most of list methods do not return anything.
print(numbers)
numbers.append(2000)
# numbers.clear()
# print(numbers)
# del numbers
# print(countries)
"""
n2 = numbers.copy()
print("numbers =", numbers)
print("n2 =", n2)
n1 = numbers
print("n1 =", n1)
numbers.clear()
print("numbers =", numbers)
print("n2 =", n2)
print("n1 =", n1)
"""
# n3 = [100, 200, 300]
n3 = "Ashesh"
print(numbers.count(11))
# numbers.append(n3)
numbers.extend(n3)
print(numbers)
print(list("Lists have less methods than strings."))
print(numbers.index(-56))
print(numbers.index(11))
print(numbers.index(11, 6))
# print(numbers.index(11, 8, 11))       lists don't have .find() method
numbers.insert(5000, 7)
print(numbers)