# bank2.py
# Author: Joanne Feeney
# This script defines a class BankAccount that has methods for depositing, withdrawing & displaying account inf
# It creates a new BankAccount object with an initial balance of $100 
# It interacts with the account by making a deposit, making a withdrawal, and displaying the balance and account information


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
    
    def display_balance(self):
        print(f"Account balance is {self.balance}.")
        
    def display_account_info(self):
        print(f"Account number: {self.account_number}\nAccount balance: {self.balance}")
        
# create a new BankAccount object with initial balance of $100
my_account = BankAccount("123456789", 100)

# interact with the account
my_account.deposit(50)
my_account.withdraw(25)
my_account.display_balance()
my_account.display_account_info()
