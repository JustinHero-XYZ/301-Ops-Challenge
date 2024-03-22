###Powershell Interpreter###

# Author: Justin Patterson
# Date last revised: 03/14/2024
# Ops Challenge #: Seattle-Ops-301w10 Ops Challenge 13
# Purpose: Powershell Automation script that adds to AD
# Script Name: powershell_automation_301w10.ps1

# Add user, title, office, department, email
New-ADUser -Name "Fraz Ferdinand" -Title "TPS Reporting Lead" -Office "Springfield, OR" -Department "TPS" -EmailAddress "franzferdinand@globexpower.com"

# End
