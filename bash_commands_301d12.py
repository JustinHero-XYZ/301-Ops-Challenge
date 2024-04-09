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
# Author: Justin Patterson
# Date last revised: 04/01/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 06
# Purpose: Execute Bash Commands with Python
# Script: bash_commands_ops301d12.py

import os

# Declare and reference variables
command1 = "whoami"
command2 = "ip a"
command3 = "lshw -short"

# Execute bash commands usind os.system()
print("Executing bash commands:")

# Execute 'whoami' command
print("\nOutput of 'whoami' command:")
os.system(command1)

# Execute 'ip a' command
print("\nOutput of 'ip a' command:")
os.system(command2)

# Execute 'lshw -short' command
print("n\Output of 'lshw -short' command:")
os.system(command3)

# End
