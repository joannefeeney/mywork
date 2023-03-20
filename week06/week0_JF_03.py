# week 06 lab
# Author: Joanne Feeney
# This program is used to answer week 06's lab questions

# the array we store everything in

'''
Commenting this out 

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
 # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
 # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules
def doView(students):
 # we fill this in later
    print(students)
#main program
students = []
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lamda functions
 # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
'''

'''
7. Ok I am going to be mean and say how would you do the doView()
function?
You can approach it the same way we did do add, just print out all the
student names first and then make a function called displayModules() and
call that after to print each name
'''

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print(f"\t{ module['name']} \t{ module['grade']}")
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

doView(students)
doView(students)
print (students)
