# bank4.py
# Author: Joanne Feeney
# This script prompts the user and reads in two money amounts (in cents)
# Adds the two amounts
# Prints out the answer in a human readable format 
# With a euro sign and decimal point between the euro and cent of the amount

cent1 = int(input("Enter the first amount in cent: "))
cent2 = int(input("Enter the second amount in cent: "))

total_cent = cent1 + cent2
total_euro = 0
if total_cent >= 100:
    total_euro += 1
    total_cent -= 100

print("The total amount is €{:.2f}".format(total_euro + total_cent/100))
