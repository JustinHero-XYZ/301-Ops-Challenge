# Author: Justin Patterson
# Date last revised: 03/03/2024
# Purpose: Execute Bash Commands with Python
# Why: To Learn A New Language

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
