numbers = [23, 47, 259, 7, 13, 79434488992114578964312456710, -34, 23.6, -33.8, 0, 47]
"""
print(numbers.index(-34))
print(numbers.index(47))
print(numbers.index(47, 2))
# print(numbers.index(47, 2, 8))

numbers.append(1000)
numbers.insert(5, 2000)
print(numbers)

print(numbers.pop(6))
print(numbers)

numbers.remove(47)
numbers.reverse()
"""
numbers.sort(reverse=True)
print(numbers)

# Next Class: Operators, if-else