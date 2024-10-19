"""
n = int(input("n : "))
i = 2
flag = 1
while i < n:
    if n % i == 0:
        flag = 0
        break
    i += 1
if flag == 1:
    print("Prime.")
else:
    print("Composite.")
"""
# break-else
# if-else

n = int(input("n : "))
i = 2
while i < n:
    if n % i == 0:
        print("Composite.")
        break
    i += 1
else:
    print("Prime.")