import datetime

print(dir(datetime))
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
Ashesh_birthday = datetime.date(1996, 12, 19)
print(Ashesh_birthday)
print(Ashesh_birthday.day)
print(Ashesh_birthday.month)
print(Ashesh_birthday.year)
next_financial_year = datetime.date(1997, 4, 1)
print(next_financial_year)
print(next_financial_year - Ashesh_birthday)
print(type(next_financial_year - Ashesh_birthday))
# print(Ashesh_birthday + 200)


interval = datetime.timedelta(200)
print(Ashesh_birthday - interval)

# US_time = datetime.time(18, 7, 45, 230745)
US_time = datetime.time(18, 10)
print(US_time)
print(US_time.hour)
print(US_time.minute)
print(US_time.second)
print(US_time.microsecond)

ist = datetime.time(6, 40)

# datetime.datetime
last_launch = datetime.datetime(2022, 2, 14, 16, 17)
print(last_launch)

# Today's date & time
print(datetime.datetime.today())

previous_launch = "10:24 on February 28, 2021"

# strptime
Amazonia_1 = datetime.datetime.strptime(previous_launch, "%H:%M on %B %d, %Y")
print(Amazonia_1)

# strftime
last_launch_str = datetime.datetime.strftime(last_launch, "%dth %B (%a), %Y at %I:%M %p")
print("ISRO's last launch was on", last_launch_str)