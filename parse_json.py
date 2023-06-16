# Working with JSON in Python

# High level human readable language - mostly used to transport data.

# JSON - JavaScript Object Notation
# JSON works with key/value pairs

# Parsing? Turning a string into a data structure and vice versa

# import json
#
# json = json.loads(open('example.json').read())
# value = json['name']
# print(json)
# print(value)
# print(type(json))

import json
import os

# script to make an absolute of the JSON file
script_dir = os.path.dirname(__file__)
print("The script is located at: " + script_dir)
script_absolute_path = os.path.join(script_dir, "example.json")
print("The script absolute path is:" + script_absolute_path)

# Script to parse JSON
json = json.loads(open(script_absolute_path).read())
value = json["name"]
print(value)

# Loop through the JSON
for key in json:
    value = json[key]
    print("The key and value are {} = {}". format(key, value))