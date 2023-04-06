# week 07 lab
# Author: Joanne Feeney
# This program is used to answer week 07's lab questions


# the with statement will automatically close the file when it is finished with it

with open("test-a.txt") as f:
    data = f.read()
    print (data)

# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()
# DO NOT DO IT THIS WAY

'''
Question:
Look at the program above, if the file test-a.txt does not exist. What will happen when the program runs?
'''

'''
Answer: 
I don't think anything will happen (nothing will print) if file does not exist
testing below
'''