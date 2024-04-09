#!/usr/bin/python3

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
