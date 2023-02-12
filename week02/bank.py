# hello.py
# Author: Joanne Feeney
# This program reads two money amounts, add them and prints the answer in a human readable format 
# with a euro sign and decimal point between the euro and cent of the amount 

number = int(input('please enter a number:'))
secondnumber = int(input('please enter a number:'))

answer = ({number} + {secondnumber})

print(f'{number} plus {secondnumber} is the answer')
