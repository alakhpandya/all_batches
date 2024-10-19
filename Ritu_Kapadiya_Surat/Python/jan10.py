"""
import myPackage                # wrong

myPackage.myModule.myFunc()
"""
# 1
"""
from myPackage import myModule
myModule.myFunc()
"""
# 2
"""
from myPackage import myModule as mm
mm.myFunc()
"""
# 3
"""
from myPackage.myModule import myFunc
myFunc()
"""
# 4
"""
from myPackage.myModule import myFunc as mf
mf()
"""
# 5
"""
from myPackage.subPackage import subModule
subModule.subFunc()
"""
# 6
"""
from  myPackage.subPackage.subModule import subFunc as sf
sf()
"""
# 7
"""
from myPackage.subPackage import subModule

subModule.factorial(5)
"""

import datetime

# print(dir(datetime))
# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)
# print(datetime.UTC)

ritu_bday = datetime.date(2002, 9, 10)
# print(ritu_bday)
# print(ritu_bday.day)
# print(ritu_bday.month)
# print(ritu_bday.year)
"""
uttarayan = datetime.date(2023, 1, 14)
print(ritu_bday - uttarayan)

# 22 July 2019, 09:13:12
chandrayaan2_launch = datetime.datetime(2019, 7, 22, 9, 13, 12)
# print(chandrayaan2_launch)

# 6 September 2019, 20:23
chandrayaan2_land = datetime.datetime(2019, 9, 6, 20, 23)
print("Time spent in space by Chandrayaan-2:", chandrayaan2_land-chandrayaan2_launch)
"""
"""
period = datetime.timedelta(100)
# print(ritu_bday + 100)
print(ritu_bday + period)
"""

print(f"Ritu is a very good girl. She was born on {ritu_bday}.")

print(f'Ritu is a very good girl. She was born on {ritu_bday.strftime("%B %dth, %Y (%a)")}.')

chandrayaan2_land = datetime.datetime.strptime("6 September 2019, 20:23", "%d %B %Y, %H:%M")
print(chandrayaan2_land)