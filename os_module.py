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