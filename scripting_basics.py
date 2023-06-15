# Basics of scripting in Python

# Libraries and Modules - Libraries bigger, Modules smaller.

# Seven "core" modules in Python

# import sys
#
# #Get Python version
# print(sys.version)
#
# import os
#
# # Get current working directory
# print(os.getcwdb())


#Runs an external file when executed
# import subprocess
#
# subprocess.run(["python", "hello_world.py "])

import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is" + pi_string)

import random
random = random.randrange(1, 10)
print(random)

import datetime

whatisdate = datetime.datetime.now()
print(whatisdate)

import json

x = {
    "name": "John",
    "age": 30,
    "city": "london",
}

y = json.dumps(x)

print(type(y))