# What is scripting


```python 
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
```

```python
# Using os to do things

import os

# os.system('echo "Hello World!"')

# Make and change directory

# Ceate directory
# Directory name
directory = "test_dir"
# Parent dir name
parent_dir = "C:/Users/tazjo/PycharmProjects/tech241"
#Path
path = os.path.join(parent_dir, directory)

# Create DIR
# os.mkdir(path)
# Putting a new file in the new dir
filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "Contents of file is written here"
    file1.write(toFile)

print(f"File {filename} created in {directory} folder ")

```