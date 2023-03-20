# week 06 lab
# Author: Joanne Feeney
# This program is used to answer week 06's lab questions

'''
Last week I got you to make a complicated data structure called student which has
two attributes, name and modules which has an array of modules and grades.
This week as an exercise I would like to create a program that allows a user to
create new students and to view students. This will be a big program for you.
So, we should break it up into smaller bits (this is where functions come in handy)
'''

'''
2. Write a function that prints out a menu of commands we can perform, ie add,
view and quit. The function should return what the user chose.
Test the function. We dont need to worry about error handling yet
'''

'''
What would you like to do?
 (a) Add new student
 (v) View students
 (q) Quit
Type one letter (a/v/q):d
you chose d
'''
#commenting question 2 out here

# def displayMenu() :
#     print("What would you like to do?")
#     print("(a) Add new student")
#     print("(v) View students")
#     print("(q) Quit")
#     choice = input("Type one letter (a/v/q):").strip()
# 
#     return choice


# choice = displayMenu()
# print(f"you chose { choice }")

'''
3. We will now use that function. Create a program that keeps displaying the
menu until the user picks q. if the user chooses a then call a function called
doAdd() if the user chooses v then call a function called doView().
(I copied the function from the last function into this program)
'''

'''
What would you like to do?
 (a) Add new student
 (v) View students
 (q) Quit
Type one letter (a/v/q):a
in adding
What would you like to do?
 (a) Add new student
 (v) View students
 (q) Quit
Type one letter (a/v/q):q
(base) andrews-MacBook-Pro:topic06-functions andrewbeatty$
'''

# using above function

def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice
def doAdd():
 # we fill this in later
 print("in adding")
def doView():
 # we fill this in later
 print("in viewing")
#main program
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lambda functions
 # I am keeping this basic for the moment
 if choice == 'a':
    doAdd()
 elif choice == 'v':
    doView()
 elif choice !='q':
    print("\n\nplease select either a,v or q")
 choice=displayMenu() 

'''
4. We can now write the function doAdd(students). So we need to think what
we want this to do.
a. Read in the students name (that is straightforward)
b. Read in the module names and grades (this is a bit more complicated
so lets put this in separate function and think about it by itself, see 5.
below)
c. Test this function, it creates a student dict, we can print that out.
d. We should add the student dict to list (pass this list in)
e. Test this.

enter name :Andrew
enter name :Mary
[{'name': 'Andrew', 'modules': []}, {'name': 'Mary',
'modules': []}]
'''

students= []
def readModules():
    return []
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

#test
doAdd(students)
doAdd(students)
print (students)

'''
5. We can now think about how to read in the modules. We want to keep
reading modules until the user enters a module name of blank.

enter name :Andrew
 enter the first Module name (blank to quit) :Programming
 enter grade:45
 enter next module name (blank to quit) :History
 enter grade:90
 enter next module name (blank to quit) :
enter name :Mary
 enter the first Module name (blank to quit) :
[{'name': 'Andrew', 'modules': [{'name': 'Programming', 'grade': 45}, {'name': 'History',
'grade': 90}]}, {'name': 'Mary', 'modules': []}]

Doesnt the data structure look ugly, and hard to read. Maybe I should have done the
function to view it before the function to add new ones!!
'''

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
 # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
 # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules
