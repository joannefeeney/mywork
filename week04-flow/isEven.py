# isEven.py
# Author: Joanne Feeney
# This program asks the user to enter in a number, and it will tell the user if the number is even or odd

number = int(input("enter an integer:"))
if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")
