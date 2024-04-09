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
# Date last revised: 04/02/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 08
# Purpose: How to work with lists in Python
# Script Name: python_lists_301d12.py

# Import libraries

import os

# Declaration of variables
### Assign a list of ten string elements to a variable
my_list = ["apple", "banana", "orange", "grape", "kiwi", "pear", "peach", "plum", "cherry", "melon"]

# Main

### Print list
print("Entire list:", my_list)

### Print the fourth element of the list
print("Fourth element:", my_list[3])

### Print the sixth through tenth element of the list
print("Sixth through tenth elements:", my_list[5:])

### Change the value of the seventh element to "onion"
my_list[6] = "onion"

### Print the modified list
print("Modified list:", my_list)

# End
