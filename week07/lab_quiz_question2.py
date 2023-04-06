# week 07 lab
# Author: Joanne Feeney
# This program is used to answer week 07's lab questions


# the with statement will automatically close the file when it is finished with it

with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written
    print (data)
with open("test-b.txt", "w") as f2: #open file again
    data = f2.write("another line\n")
    print (data)

'''
Question 1:
Look at the program above, if the file test-b.txt does not exist, what will be
outputted to the console when this program is run?

Question 2:
What will the contents of the file test-b.txt be when this program is run?
'''

'''
Answer:
1. The terminal will advise that the file does not exist

2. I don't know...
'''