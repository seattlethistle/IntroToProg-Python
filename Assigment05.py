# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SDH,11.16.20,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file (I modified the name)
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: DONE
try:
    objFile = open(strFile, "r")

    for row in objFile:
        lstRow = row.split(",")  # Return a list
        dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}  # Strip spaces
        lstTable.append(dicRow)
    objFile.close()
    print("Current Task list (if blank the Task List is empty): ")
    print(lstTable)
except:
    print("The file 'ToDoList.txt' has not been created yet.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: DONE
        print("Current Task list (if blank the Task List is empty): ")
        for row in lstTable:
            strTask = row["Task"]
            strPriority = row["Priority"]
            print("Task: ", strTask, ", Priority: ", strPriority, sep="")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: DONE
        # Get User Input
        strTaskInp = input("Enter an task name: ").lower() # writing everything as lower case
        strPriorityInp = input("Give it a priority: ").lower()
        # In line above could insert options for user to pick from (1-5 or Low-High)
        dicRow = {"Task": strTaskInp, "Priority": strPriorityInp}
        lstTable.append(dicRow)
        for objRow in lstTable:
            print(objRow)
        # Process the data
        objFile = open(strFile, "w")  # open the file name by the str variable defined above
        objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')  # write the list
        objFile.close()
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: DONE
        remTask = input("Which Task? ").lower().strip() # Case insensitive dictionary search
        # Note: after inserting this case check, it became clear it would be easier to change
        # all tasks either saved the file or printed to screen to lower case.
        # However ideally it wouldn't matter which case was used.
        count = 0
        for row in lstTable:
            if remTask == row["Task"]:
                lstTable.remove(row)
                count += 1
        if count == 0:
            print("I'm sorry, that task doesn't exist.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: DONE
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("File has been saved.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: DONE
        # Nothing extra required here as starter code included the break statement
        break  # and Exit the program





