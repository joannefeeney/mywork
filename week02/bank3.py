# bank3.py
# Author: Joanne Feeney
# This script prompts the user and reads in two money amounts 
# Adds the two amounts
# Prints out the answer in a human readable format 
# With a euro sign and decimal point between the euro and cent of the amount

# prompt the user for the first amount in euro and cent
euro1 = int(input("Enter the first amount in euro: "))
cent1 = int(input("Enter the first amount in cent: "))

# prompt the user for the second amount in euro and cent
euro2 = int(input("Enter the second amount in euro: "))
cent2 = int(input("Enter the second amount in cent: "))

# add the euro and cent amounts
total_euro = euro1 + euro2
total_cent = cent1 + cent2

# if the total cent amount is greater than 100, adjust the euro and cent amounts accordingly
if total_cent >= 100:
    total_euro += 1
    total_cent -= 100

# print out the result with a euro sign and decimal point between the euro and cent amounts
print("The total amount is €{:.2f}".format(total_euro + total_cent/100))
