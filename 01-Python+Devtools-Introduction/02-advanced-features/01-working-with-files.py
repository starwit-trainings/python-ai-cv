# examples how to work with files
import os
from os import walk

def readFromFile(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        print(f.read()) # is that a good idea, if file is big?
        f.close() # be nice to your operating system
    else:
        print("File", filename, "doesn't exist")

filename = "samplefile"
readFromFile(filename)

# create and overwrite
f = open(filename, "w") # see https://www.w3schools.com/python/python_file_handling.asp
f.write("This is content, writen to file, replacing all existing content - careful!\n")
f.close()

readFromFile(filename)

# append content to existing file
f = open(filename, "a") # see https://www.w3schools.com/python/python_file_handling.asp
f.write("This is content, appended to file. All existing content is preserved")
f.close()

readFromFile(filename)

# list files/folders
for (dirpath, dirnames, filenames) in walk('.'):
    print(dirnames)
    print(filenames)
    break

# how to delete a file
os.remove(filename)