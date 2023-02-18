# guess1.py
# Author: Joanne Feeney
# This program prompts the user to guess a number
# The program should keep prompting the user to guess the number until the user gets the right one

numberToGuess = 30

guess = int (input("please guess the number:"))
while guess != numberToGuess:
    print ("Wrong") 
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)
