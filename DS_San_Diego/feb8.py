l3 = [12, 15.43, ["Mumbai", 10, -0.75], "San Diego", 11.22, "Ahmedabad", -26.4, 0, "USA", 33, "India", 45, 59]

# Slicing always returns a copy of the original collection
"""
# print(l3[-3])
# print(l3[3 : 7])
# print(l3[1 : 12 : 2])
# print(l3[11 : 1 : -2])

print(l3.append(6000))
# print(l3)
# l3.append(6000)[2]      This will not work as append() does not return anything
# l4 = l3.append(6000)      
# l4[2]                     Even this will not work

print(f"Before: {len(l3)}")         # 14
l3.append(["Hello", "World!"])
print(f"After: {len(l3)}")          # 15

l3.clear()
print(l3)

# del l3

# print(l3)

l3.append("Krushy")
print(l3)

l3 = [1,2,3,4]
"""

l3 = [12, 15.43, ["Mumbai", 10, -0.75], "San Diego", 12, "Ahmedabad", -26.4, 0, "USA", 12, 33, "India", 45, 12, 59]
l4 = l3.copy()      # Deep Copy
l5 = l3             # Shallow Copy
# print("l3 =", l3)
# print("l4 =", l4)
# print("l5 =", l5)

print(l3.count(12))
# l3.append(["Hello", "World!"])
l3.extend(["Hello", "World!"])
print(l3)