# write mode
# fp = open("user_data.txt", "w")
# if fp.writable():
#     print("Writing is enabled in this file.")
# direct write
# fp.write("Sr_no,Name,User name,Password\n")
# writing through variables
"""
print("Enter the following details of 6 users:")
user_info = ["Sr_no,Name,User name,Password\n"]
for sr_no in range(1, 7):
    print(f"User-{sr_no}:")
    name = input("Name: ")
    userName = input("User Name: ")
    password = input("Password: ")
    # fp.write(f"{sr_no},{name},{userName},{password}\n")
    user_info.append(f"{sr_no},{name},{userName},{password}\n")
print(user_info)
fp = open("user_data.txt", "w")
fp.writelines(user_info)
fp.close()
"""
fp = open("user_data.csv", "rt")
# content = fp.read(20)
# print(content)
# print(fp.read())
# print(fp.readline())
# print(fp.tell())
# fp.seek(65)
# print(fp.readline())
user_details = fp.readlines()
print(user_details)
print(fp.readable())
print(fp.writable())
fp.close()
user5 = user_details[5].split(",")
print("user name: ", user5[2])