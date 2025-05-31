"""
s1 = {"apple", "mango", "banana", "cherries", "kiwi"}
# s1.discard("banana")

# ele = s1.pop()        # Removes an arbitrary element from the set
# print(ele)

# s1.remove("cherries")
# s1.discard("papaya")
# s1.remove("papaya")

f = {"watermelon", "muskmelon", "guava", "apple", "mango"}
s1.update(f)

print(s1)
"""

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9,10}
s3 = {9,10,11,12,13}

# uni = s1.union(s2)
# print(uni)
# print(s1)
# print(s2)

# inter = s1.intersection(s2)
# print(inter)

# s1 = s1.intersection(s2)
# inter = s1.intersection_update(s2)
# print(inter)
# print(s1)

s1.update(s2)