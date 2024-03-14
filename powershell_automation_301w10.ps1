###Powershell Interpreter###

# Author: Justin Patterson
# Date last revised: 03/14/2024
# Ops Challenge #: Seattle-Ops-301w10 Ops Challenge 13
# Purpose: Powershell Automation script that adds to AD
# Script Name: powershell_automation_301w10.ps1

# Define user attributes
$FirstName = "Franz"
$LastName = "Ferdinand"
$DisplayName = "$FirstName $LastName"
$SamAccountName = "ferdinandf"
$UserPrincipalName = "$SamAccountName@yourdomain.com"
$Title = "TPS Reporting Lead"
$Department = "TPS Department"
$Office = "Springfield, OR"
$Company = "Globex USA"
$Email = "ferdi@globexpower.com"
$Password = "P@ssw0rd123"

# Define group attributes
$GroupName = "TPS Department"
$GroupDescription = "OU for TPS Department employees"

# Define OU attributes
$OUName = "Sringfield"
$OUDescription = "OU for Springfield office"

# Create group
New-AdGroup -Name $GroupName -Description $GroupDescription -GroupScope Global -Path "OU=$OUName,DC=yourdomain,DC=com"

# Create user in Active Directory
New-ADUser `
    -SamAccountName $SamAccountName `
    -UserPrincipalName $UserPrincipalName `
    -Name $DisplayName `
    -GivenName $FirstName `
    -Surname $LastName `
    -DisplayName $DisplayName `
    -Title $Title `
    -Department $Department `
    -Office $Office `
    -Company $Company `
    -EmailAddress $Email `
    -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force)
    -Enabled $true
    -Path "OU=OUName,DC=yourdomain,DC=com"

# Add user to group
Add-AdGroupMember -Identity $GroupName -Members $SamAccountName

Write-Host "User '$DisplayName', group 'GroupName', and OU 'OUName' created successfully."

# End
