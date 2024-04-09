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
# Date last revised: 04/08/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 11
# Purpose: Create python script that fetches info using Psutil
# Script Name: psutil_301d12.py

# Import libraries
import psutil

# Declaration of functions
def get_system_times():
    try:
        # Get system times
        system_times = psutil.cpu_times()
        
        # Print the collected information
        print("Time spent by normal processes executing in user mode:", system_times.user)
        print("Time spent by processes executing in kernel mode:", system_times.system)
        print("Time when system was idle:", system_times.idle)
        print("Time spent by priority processes executing in user mode:", system_times.nice)
        print("Time spent waiting for I/O to complete:", system_times.iowait)
        print("Time spent for servicing hardware interrupts:", system_times.irq)
        print("Time spent for servicing software interrupts:", system_times.softirq)
        print("Time spent by other operating systems running in a virtualized environment:", system_times.steal)
        print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", system_times.guest)
    except Exception as e:
        print("Error:", e)

# Main
get_system_times()
