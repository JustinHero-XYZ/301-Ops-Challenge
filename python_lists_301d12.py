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
