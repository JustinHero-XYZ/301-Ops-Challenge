#1/bin/bash

# Script Name: permissions.sh
# Author: Justin Patterson
# Date of latest revision: 02/22/2024
# Purpose: change permissions

# Prompt user for input directory path
echo "Enter directory path:"
read directory_path

# Prompt user for input permissions number
echo "Enter the permissions number (e.g. 777):"
read permissions

# Change permissions for files in the directory
chmod -R "$permissions" "$directory_path"

# Print directory contents and new permission settings
echo "Directory contents:"
ls -l "$directory_path"

# End