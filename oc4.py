# Objectives

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run

# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.

# This will not run on windows needs to be mac or linux due to os being bash

import subprocess
import os

# Define the bash commands as variables
whoami_command = "whoami"
ip_a_command = "ip a"
lshw_command = "lshw -short"

# Print description of each command
print("Running 'whoami' command:")
# Use os.system() for basic execution
os.system(whoami_command)

print("\nRunning 'ip a' command:")
# Use subprocess.run() for more flexibility
subprocess.run(ip_a_command, shell=True)

print("\nRunning 'lshw -short' command:")
# Use subprocess.Popen() for even more control
process = subprocess.Popen(lshw_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout.decode())
