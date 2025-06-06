"""
import datetime

chandrayaan2 = "July 22, 2019 at 02:43 PM"
launch_date = datetime.datetime.strptime(chandrayaan2, "%B %d, %Y at %I:%M %p")
print(launch_date)

agni5 = datetime.datetime(2021, 10, 27, 19, 50, 0)
print(agni5)
print(datetime.datetime.strftime(agni5, "The Agni-V missile was first successfully test fired on %A, %d %b, %Y at %I:%M:%S %p"))
message1 = "The Agni-V missile was first successfully test fired on {:%d/%m/%y}"
message2 = "at {:%I:%M:%S %p}"
print(message1.format(agni5) + " " + message2.format(agni5))
"""
import random

# print(dir(random))
for i in range(10):
    print(random.random())