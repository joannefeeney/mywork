# week 07 lab
# Author: Joanne Feeney
# This program counts how many times it was run

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

# test it
num = readNumber()
print (num)
