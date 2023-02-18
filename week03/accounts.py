# accounts.py
# Author: Joanne Feeney
# This script reads in a 10 character account number
# It outputs the account number with only the last 4 digits showing and the first 6 digits replaced with X

# Ask user for input
account_number = input("Enter your 10-digit account number: ")

# Replace first 6 digits with X
masked_account = "X" * 6 + account_number[6:]

# Extract last 4 digits
last_4_digits = masked_account[-4:]

# Print masked account number
print("Your masked account number is:", masked_account)

# This program first prompts the user to enter their 10-digit account number using the input() function. 
# It then creates a new string called masked_account by replacing the first 6 characters of the input with "X" 
# It uses string multiplication and concatenation.
# Next, it extracts the last 4 digits of the masked_account string 
# It uses slicing and the negative index -4. 
# Finally, it prints the masked account number to the console using the print() function