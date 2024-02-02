# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
from urllib import response
import requests
#b = input("Get, Post, Put, Delete , Head, Patch, Options:")

import requests

# Prompt the user for destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP method
http_method = input("Select HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Create a dictionary to map HTTP status codes to plain terms
status_code_mapping = {
    200: 'OK',
    201: 'Created',
    204: 'No Content',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error'
}

# Display the entire request before sending and ask for confirmation
print(f"\nPreparing to send {http_method} request to {url}")
confirmation = input("Do you want to proceed? (y/n): ")

if confirmation.lower() != 'y':
    print("Request canceled.")
else:
    # Perform the HTTP request
    response = requests.request(http_method, url)

    # Print the entire request details
    print("\nRequest Details:")
    print(f"URL: {url}")
    print(f"Method: {http_method}")
    
    # Display response header information
    print("\nResponse Header Information:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Translate status code into plain terms
    status_code = response.status_code
    plain_status = status_code_mapping.get(status_code, 'Unknown Status')
    print(f"\nStatus Code: {status_code} - {plain_status}")

    # Display the response content
    print("\nResponse Content:")
    print(response.text)
