# Error Handling/Exception Handling
"""
# while True:
try:
    a = int(input("Enter two integers:\n"))
    b = int(input())
    print("Division =", a/b)
    loop = input("Press 'x' to quit, 'Enter' to repeat: ").lower()
    
except ZeroDivisionError:
    print("Oops! It seems that you are trying to divide by zero!")
# except ValueError:
#     print("Please enter integers only...")


# except:
    # print("Sorry, something went wrong...")
    

# except Exception as e:
    # print("Sorry, something went wrong...")
    # print(e)

else:
    print("Whatever you write here, will be executed if no exception is raised.")

finally:
    print("This will be executed no matter what.")

print("This is not inside try-except-else-finally block.")
"""
# The columns will be sr.no, album, artist, genre

offset = 1
while True:
    choice = input("Enter choice [R/W/X]").lower()  
    if choice == 'r':
        sr_no = int(input("Sr_no: "))
        try:
            f = open("music.csv")
            data = f.readlines()
            f.close()
        except FileNotFoundError:
            print("No such file exists. First create it.")
        else:
            info = data[offset+sr_no].split(',')
            print("Sr_no: "+info[0])
            print("Album: "+info[1])
            print("Artist: "+info[2])
            print("Genre: "+info[3])
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
        data = f.readlines()
        f.close() 
        srNo = len(data) - offset
        data.append(f"\n{srNo},{album},{artist},{genre}")
        f = open("music.csv","w")
        data = f.writelines(data)
        f.close() 
    elif choice=='x':
        break