#!/bin/bash

# Script Name: clearing_logs_301w10.sh
# Author: Justin Patterson
# Date of latest revision: 02/27/2024
# Purpose: Clearing Logs

# Print original file sizes
echo "Original file sizes before compression:"
echo "Size of /var/log/syslog:"
du -h /var/log/syslog
echo "Size of /var/log/wtmp:"
du -h /var/log/wtmp

# Define backup directory
backup_dir="/var/log/backups"

# Ensure backup directory exists
sudo mkdir -p "$backup_dir"

 # Compress and backup log files with timestamp
timestamp=$(date +%Y%m%d%H%M%S)
sudo gzip -c /var/log/syslog >"$backup_dir/syslog-$timestamp.zip"
sudo gzip -c /var/log/wtmp > "$backup_dir/wtmp-$timestamp.zip"

# Clearing log files
echo "Clearing log files..."
truncate -s 0 /var/log/syslog
truncate -s 0 /var/log/wtmp

# Print compressed file sizes
echo "Compressed file sizes:"
echo "Size of $backup_dir/syslog-$timestamp.zip"
du -h "$backup_dir/syslog-$timestamp.zip"
echo "Size of $backup_dir/wtmp-$timestamp.zip"
du -h "$backup_dir/wtmp-$timestamp.zip"

# Compare sizes
original_syslog_size=$(stat -c %s /var/log/syslog)
compressed_syslog_size=$(stat -c %s "$backup_dir/syslog-$timestamp.zip")
original_wtmp_size=$(stat -c %s /var/log/wtmp)
compressed_wtmp_size=$(stat -c %s "$backup_dir/wtmp-$timestamp.zip")

echo "Comparison of file sizes:"
echo "Original syslog size: $original_syslog_size bytes"
echo "Compressed syslog size: $compressed_syslog_size bytes"
echo "Original wtmp size: $compressed_wtmp_size bytes"
echo "Compressed wtmp size $compressed_wtmp_size bytes"

#End




