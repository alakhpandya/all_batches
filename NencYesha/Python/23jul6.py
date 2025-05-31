# papa = pip install

# import speech_recognition as sr


# Some useful built in modules of python
import datetime

# print(dir(datetime))
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

# print(datetime.UTC)

nencYesha = datetime.date(2024, 1, 26)
# print(nencYesha)
# print(nencYesha.day)
# print(nencYesha.month)
# print(nencYesha.year)

alakh = datetime.date(2024, 8, 20)
# print(alakh)

# print(alakh - nencYesha)
gap = datetime.timedelta(100)
# print(nencYesha + gap)

# c2 = datetime.datetime(2019, 7, 19, 2, 51, 30)
# print(c2)

# interval = datetime.timedelta(90, 0, 0, 0, 30, 5)
interval = datetime.timedelta(90, hours=5, minutes=30)
# print(c2 + interval)

"""
26th Jan, 2024 (Thursday)
Jan 26, 2024 (Thu) 9:00pm
26 Jan 24, Thu
"""
"""
nY = datetime.datetime(2024, 1, 26, 21)
# print(nY)
nY_str = datetime.datetime.strftime(nY, "%b %d, %Y (%a) %I:%M %p")
print(nY_str)

ch2 = "15 July 2019 at 02:51 am"
c2 = datetime.datetime.strptime(ch2, "%d %B %Y at %I:%M %p")
print(c2)

print(datetime.datetime.today())
print(datetime.datetime.now())
"""
"""
import time

t1 = time.time()
a = 0
for i in range(10000):
    for j in range(10000):
        a += 1
t2 = time.time()
print("Execution time:", t2 - t1)
"""

# Next: random module