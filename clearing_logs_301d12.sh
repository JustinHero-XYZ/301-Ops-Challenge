#!/bin/bash

# Script Name: clearing_logs_301d12.sh
# Author: Justin Patterson
# Date of latest revision: 03/29/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 05
# Purpose: Clearing Logs

# Define the backup directory
backup_dir="backups"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Get the current timestamp
timestamp=$(date +"%Y-%m-%d %H%M%S")

# Array of log files to process
log_files=(/var/log/syslog /var/log/wtmp)

# Loop through each log file
for logfile in "${log_files[@]}"; do
    # Print file size before compression
    echo "File size of $logfile before compression:"
    du -sh "$logfile"

    # Compress the log file to the backup directory with timestamp
    sudo gzip -c "$logfile" > "$backup_dir/$(basename "$logfile")-$timestamp.gz"

    # Clear the contents of the log file
    sudo sh -c "cat /dev/null > $logfile"

    # Print file size after compression
    echo "File size of $(basename "$logfile") after compression:"
    du -sh "$backup_dir/$(basename "$logfile")-$timestamp.gz"
done

# Compare the sizes of original log files and compressed files
echo "Comparison of file sizes:"
for logfile in "${log_files[@]}"; do
    original_size=$(stat --format=%s "$logfile")
    compressed_size=$(stat --format=%s "$backup_dir/$(basename "$logfile")-$timestamp.gz")
    echo "Original $(basename "$logfile") size: $original_size"
    echo "Compressed $(basename "$logfile") size: $compressed_size"
done

#End