offset = 5

def readFile():
    file = open("batch.csv", "r")
    dataset = file.readlines()
    file.close()
    return dataset

def generateSrNo():
    srNo = len(dataset) - offset
    return srNo

def writeIntoFile():
    file = open("batch.csv", "w")
    file.writelines(dataset)
    file.close()

def adjustSrNo(dataset):
    row_count = 0
    for row in dataset:
        if row_count > offset:
            old_row = row.split(",")        # ["1", "Alakh", "Teacher"]
            new_row = str(row_count-offset) + "," + old_row[1] + old_row[2]
            dataset.pop(row_count)
            dataset.insert(row_count, new_row)
        row_count += 1
    return dataset

count = 0
dataset = readFile()
while True:
    print("Press 1 to add a new member")
    print("Press 2 to delete a member")
    print("Press 3 to view details of a member")
    print("Press 4 to save & exit")
    print("Press 5 to exit without saving the changes")
    choice = int(input())
    if choice == 1:
        srNo = generateSrNo()
        name = input("Please enter the following details:\nName: ")
        role = input("Role: ")
        dataset.append("\n" + str(srNo) + "," + name + "," + role)
        print("Member added successfully!")
        count += 1
    elif choice == 2:
        lineNo = int(input("Enter the serial number: ")) + offset
        dataset.pop(lineNo)
        print("Member deleted successfully!")
        count += 1
    elif choice == 3:
        lineNo = int(input("Enter the serial number: ")) + offset
        srNo, name, role = dataset[lineNo].split(",")
        print(f"Sr.No.:\t{srNo}\nName:\t{name}\nRole:\t{role}")
    elif choice == 4:
        dataset = adjustSrNo(dataset)
        writeIntoFile()
        print(f"{count} operations performed and saved successfully!")
        break
    elif choice == 5:
        print(f"{count} operations were performed but not saved...")
        break