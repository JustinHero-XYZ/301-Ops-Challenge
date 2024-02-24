#!/bin/bash

# Script Name: Conditionals_301w10.sh
# Author: Justin Patterson
# Date of latest revision: 02/23/2024
# Purpose: Launch system menu

while true; do
    # Display menu options
    echo "Menu Options:"
    echo "1. Hello World! (Prints "Hello World!" to the screen)"
    echo "2. Ping self (pings this computer's loopback address)"
    echo "3. IP info (print the network adapter information for this computer)"
    echo "4. Exit"

    # Prompt user for input
    read -p "Please enter your choice (1-4): " choice

    # Use a conditional statement to evaluate user input
    if [ "$choice" == "1" ] ; then
        echo "Hello World!"
    elif [ "$choice" == "2" ] ; then
        ping -c 4 127.0.0.1
    elif [ "$choice" == "3" ] ; then
        ip a
    elif [ "$choice" == "4" ] ; then
        echo "Exiting Program."
        break
    else
        echo "Invalid choice. Please enter a number between 1 and 4."
    fi
done

