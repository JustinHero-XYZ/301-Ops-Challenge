#!/usr/bin/env python3

# Author: Justin Patterson
# Date last revised: 04/04/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 09
# Purpose: Create if statements using the logical conditionals below
# Script Name: python_conditionals_301d12.py

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

# Import libraries

# Define variables
a = 5
b = 10

# Equals: a == b
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Not Equals: a != b
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# Less than: a < b
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# Less than or equal to: a <= b
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is not less than or equal to b")

# Greater than: a > b
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Greater than or equal to: a >= b
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is not greater than or equal to b")

# First if statement with if and elif
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")

# Second if statement with if, elif, and else
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is not greater than b and not equal to b")

# End
