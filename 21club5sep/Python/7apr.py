# 3. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.
"""
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
word = input("Enter the word you want to sort with: ")  # bug
sorted_list = []
for string in list1:
    sorted_list.append(str(string.count(word)) + "_" + string)
sorted_list.sort()
sorted_list.reverse()
final_list = []
for string in sorted_list:
    final_list.append(string.split("_")[1])
print(final_list)
"""
# Functions in Python
def average(n1, n2):
    ans = (n1 + n2)/2
    return ans

print("Enter two integers:")
a = int(input())
b = int(input())
average(a, b)
