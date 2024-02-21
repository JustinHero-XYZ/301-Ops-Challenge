#!/bin/bash

# Script Name: ops301w10-challenge02.sh
# Author: Justin Patterson
# Date of latest revision: 02/20/2024
# Purpose: Append; Date and Time

# Print timestamped echo statement indicating script start
echo "$(date +%Y-%m-%d-%T): Starting script..."

# Copy /var/log/syslog to the current working directory
cp /var/log/syslog ./syslog_copy

# Get current date and time
current_date=$(date +"%Y-%m-%d_%H-%M-%S")

# Append current date and time to filename
new_filename="syslog_${current_date}"
mv syslog_copy "${new_filename}"

# Print timestamped echo statement showing script is complete
echo "$(date +"%Y-%m-%d %T"): Script completed successfully!"

#End