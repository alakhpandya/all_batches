# Functions: Helpers
"""
Cleaner:
without argument, without return

Potato vendor:
without argument, with return

Telecaller:
with argument, without return

Mathemacian to find average:
with argument, with return
"""

def myTown():
    print("\nSan Diego is a city on the Pacific Ocean coast in Southern California located immediately adjacent to the Mexico–United States border.\nWith a population of over 1.3 million residents, the city is the eighth-most populous in the United States and the second-most populous in the state of California after Los Angeles.\nThe city is the seat of San Diego County, which has a population of nearly 3.3 million people as of 2021.\nSan Diego is known for its mild year-round Mediterranean climate, extensive beaches and parks, its long association with the United States Navy, and its recent emergence as a healthcare and biotechnology development center.\n")

a = int(input("a: "))
b = int(input("b: "))

if a > b:
    myTown()

if a/b > 1:
    myTown()

if a%b != 0:
    myTown()

if a-b > 0:
    myTown()