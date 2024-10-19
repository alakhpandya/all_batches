import csv
"""
f = open('music.csv')
data = csv.reader(f)
heading = next(data)
for row in data:
    print(row)

print(heading)
f.close()
"""

while True:
    choice = input("Enter choice [R/W/X]").lower()  
    if choice == 'r':
        sr_no = int(input("Sr_no: "))
        try:
            f = open("music.csv")
            reader = csv.reader(f)
            next(reader)
            data = []
            for row in reader:
                data.append(row)
            f.close()
        except FileNotFoundError:
            print("No such file exists. First create it.")
        else:
            print("Sr_no: "+data[sr_no][0])
            print("Album: "+data[sr_no][1])
            print("Artist: "+data[sr_no][2])
            print("Genre: "+data[sr_no][3])
    elif choice == 'w':
        album = input("Album: ")
        artist = input("Artist: ")
        genre = input("Genre: ")
        try:
            f = open("music.csv", "x")
            f.write("Sr.No.,Album,Artist,Genre")
            f.close()
        except FileExistsError:
            pass
        f = open("music.csv")
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        f.close()
        srNo = len(data) - 1
        data.append([f'"{srNo}","{album}","{artist}","{genre}"'])
        f = open("music.csv","w")
        for album_list in data:
            f.writelines(album_list)
            f.write('\n')
        f.close() 
    elif choice=='x':
        break


# Next Class: Resource Management


