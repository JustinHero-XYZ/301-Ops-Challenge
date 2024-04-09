#!/usr/bin/python3

# Author: Mr. Robot
# Date last revised: 03/15/2024
# Ops Challenge #: Seattle-Ops-301w10 Ops Challenge 14
# Purpose: Python malware script analysis
# Script Name: malware_analysis_301w10.py

###All lines with '###' are part of the script analysis and not the script itself

###Importing modules
import os
import datetime

###Defines a constant variable SIGNATURE with value "VIRUS"
SIGNATURE = "VIRUS" 

###Function to recursively search for Python files in a directory
def locate(path):
    ###List to store targeted files
    files_targeted = []
    ###Gets list fo files/directories in the specified path
    filelist = os.listdir(path)
    ###Iterates through each file/directory
    for fname in filelist:
        ###If it's a directory, recursively call locate function
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
            ###If it's a Python file
        elif fname[-3:] == ".py":
            infected = False
            ###Opens the file and checks if SIGNATURE exists in any line
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
                ###If file is not infected, adds it to the list
            if infected == False:
                files_targeted.append(path+"/"+fname)
#!/usr/bin/env python3

# Author: Justin Patterson
# Date last revised: 04/05/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 10
# Purpose: File handling operations in Python
# Script Name: file_handling_301d12.py

# Import libraries
import os

# Declaration of variables
file_name = "example.txt"

# Declaration of functions
def file_handling():
    # Create a new .txt file
    with open(file_name, "w") as file:
        file.write("This is line 1.\n")
        file.write("This is line 2.\n")
        file.write("This is line 3.\n")

    # Append 3 lines to the file
    with open(file_name, "a") as file:
        file.write("This is line 4.\n")
        file.write("This is line 5.\n")
        file.write("This is line 5.\n")

    # Open and read the first line of the file
    with open(file_name, "r") as file:
        first_line = file.readline()
        print("First line of the file:", first_line)

    # Delete the .txt file
    os.remove(file_name)
    print("File, file_name, has been deleted.")
# Main
if __name__ == "__main__":

    ### Pass the variable into the function here
    file_handling()

# End
