#!/usr/bin/python3

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
