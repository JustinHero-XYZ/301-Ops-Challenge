#!/usr/bin/python3

# Author: Mr. Robot
# Date last revised: 04/09/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 12
# Purpose: Python malware script analysis
# Script Name: malware_analysis_301d12.py

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
# Date last revised: 04/09/2024
# Ops Challenge #: Seattle-Ops-301d12 Ops Challenge 12
# Purpose: Perform HTTP request based on user input
# Script Name: http_request_301d12.py

# Import libraries
import requests

# Declaration of variables
url = ""
http_method = ""

# Function to translate HTTP status codes to plain text terms
def translate_status_code(code):
    status_codes = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        500: "Internal Server Error"
    }
    return status_codes.get(code, "Unknown Status Code")

# Declaration of functions
def perfom_http_request(url, http_method):
    # Printing the entire request
    print(f"\nSending {http_method} request to: {url}")
    confirm = input("Confirm sending request? (yes/no): ")

    if confirm.lower() != 'yes':
        print("Request cancelled.")
        exit()

    # Performing the request
    response = requests.request(http_method, url)

    # Printing response header information
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    # Translating and printing the status code
    status_text = translate_status_code(response.status_code)
    print(f"\nStatus Code: {response.status_code} - {status_text}")

    # Printing response content
    print("nResponse Content:")
    print(response.text)

# Main
if __name__ == "__main__":
    # Read user input for destination URL
    url = input("Enter the destination URL: ")

    # Prompting user to select HTTP Method
    print("Select HTTP Method:")
    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. DELETE")
    print("5. HEAD")
    print("6. PATCH")
    print("7. OPTIONS")

    method_choice = int(input("Enter your choice (1-7): "))
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
    http_method = methods[method_choice - 1]

    # Pass the variable into the function here
    perfom_http_request(url, http_method)

# End
