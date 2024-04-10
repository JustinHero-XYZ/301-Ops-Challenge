###Powershell Interpreter###

# Author: Justin Patterson
# Date last revised: 04/10/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 13
# Purpose: Powershell Automation script that adds to AD
# Script Name: powershell_automation_301d12.ps1

# Define user details
$Name = Read-Host "Enter Name of New User:"
$Title = Read-Host "Enter Title of New User:"
$Office = Read-Host "Enter Office Location:" 
$Department = Read-Host "Enter New User Department:"
$EmailAddress = "Enter New User Email:"

# Add user, title, office, department, email
New-ADUser -Name "$Name" -Title "$Title" -Office "$Office" -Department "$Department" -EmailAddress "$EmailAddress"

# End
