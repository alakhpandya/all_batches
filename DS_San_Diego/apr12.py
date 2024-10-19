
"""
dd={"Krushy":45,"Freny":47,"Chandresh":76,"Raju":100,"Rushabh bhaiya": 550}

# print(list(dd))
l1 = list(dd.items())
l2 = []
for stu, marks in l1:
    l2.append((marks, stu))
print(l2)
l2.sort(reverse=True)
l3 = []
for marks, stu in l2:
    l3.append((stu, marks))
print(l3)
final_dict = dict(l3)
print(final_dict)
"""
"""
8.  Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

for example:
list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input string = 'bug'
output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

input string = 'bun'
output list = ['bug bun bug bun bug bug', 'bunny bug', 'no bun', 'buggy bug bug buggy']
"""
"""
l1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
l2 = []
for word in l1:
    f = word.count("bug")
    l2.append((f, word))
l2.sort(reverse=True)
print(l2)
final_list = [word for f,word in l2]
print(final_list)
"""
