#!/bin/bash

# Script Name: clearing_logs_301w10.sh
# Author: Justin Patterson
# Date of latest revision: 02/27/2024
# Purpose: Clearing Logs

# Prompt user for input directory path
echo "Enter the directory path:"
read directory_path

# Check if directory exists
if [ ! -d "$directory_path" ]; then
    echo "Directory does not exist. Would you like to create it? (y/n):"
    read create_dir_choice

    if [ "$create_dir_choice" = "y" ]; then
        mkdir -p "$directory_path" || { echo "Failed to create directory. Exiting..."; exit 1; }
    else
        echo "Exiting..."
        exit 1
    fi
fi

# Prompt user for input permissions number
echo "Enter the chmod permissions number: (e.g 777):"
read permissions

# CD to the directory
cd "$directory_path"

# Change permissions for all the files in the directory
chmod -R "$permissions" .

# Print directory contents and new permissions
echo "Directory contents and new permissions settings:"
ls -l

# End



