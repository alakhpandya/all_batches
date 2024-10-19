offset = 3
while True:
    operation = input("Enter your choice- R/W/X: ").lower()
    if operation == 'r':
        roll_no = int(input("Roll No: "))
        f = open("batch.csv", "r")
        data = f.readlines()
        f.close()
        info = data[offset + roll_no].split(",")
        print("Roll No: ", info[0])
        print("Name: ", info[1])
        print("Role: ", info[2])
    elif operation == 'w':
        name = input("Name: ")
        role = input("Role: ")
        f = open("batch.csv", "r")
        data = f.readlines()
        f.close()
        roll_no = len(data) - offset
        data.append(f"\n{roll_no},{name},{role}")
        f = open("batch.csv", "w")
        f.writelines(data)
        f.close()
    elif operation == 'x':
        break
    else:
        print("Invalid Operation...")


"""
Write a Python program that helps me to store collection of my favourite music into a file. The columns will be sr.no, album, artist, genre
"""