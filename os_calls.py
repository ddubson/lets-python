__author__ = 'ddubson'

import os
from subprocess import call

# Print CWD -> Current Working Directory
print(os.getcwd())

# Print UID of user
print(os.getuid())

# Print PATH variable
print(os.getenv("PATH"))

# Execute shell call
os.system("ls -la")

# Execute shell call via thread
inp = input("Hit enter")
call(['ls', '-la'])