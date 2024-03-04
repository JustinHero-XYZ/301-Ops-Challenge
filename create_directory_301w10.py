#!/usr/bin/env python3

# Author:
# Date last revised:
# Ops Challenge #:  
# Purpose:
# Script Name:

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
