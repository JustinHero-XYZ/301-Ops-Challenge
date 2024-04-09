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
# Ops Challenge #: Seattle-Ops-301d12 Challenge 07
# Purpose: Generate directory information for a user-provided directory path.
# Script Name: dir_info_gen_301d12.py

# Import libraries

import os

# Declaration of variables
user_input = input("Enter the directory path: ")

# Declaration of functions
def generate_directory_info(user_path):
    """
    Function to generate directory information using os.walk().

    Args:
    user_path (str): The user-provided directory path.
    """
    for (root, dirs, files) in os.walk(user_path):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files==")
        print(files)

# Main
if __name__=="__main__":
    # Pass the variable into the function here
    generate_directory_info(user_input)

# End
