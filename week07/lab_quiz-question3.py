# week 07 lab
# Author: Joanne Feeney
# This program is used to answer week 07's lab questions


# The with statement will automatically close the file when it is finished with it
with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written
    print (data)
with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line\n")
     print (data)


'''
Question:
Look at the modified program above, what will the contents of the file be after this program is run
'''

'''
Answer:
I don't know...
'''