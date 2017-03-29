#!/usr/local/bin/python3

# How to open and read a file

# filehandle = open("/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/PythonNotes.txt", 'r')
# filecontent=filehandle.read()
# print(filecontent)
# print(filecontent[0])

# filehandle = open("/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/PythonNotes.txt", 'r')
# filecontent=filehandle.readlines()
#print(filecontent)
#print(filecontent[0])

# for x in filecontent:
#     print(x)
    #y = x.split(" ")
    #print(y)

# reset the "cursor" in the read/readlines back to the beginning of the file     
# filehandle.seek(0)
# filehandle.close()

# Note this will open and create a new file. To append use the 'a' option
# filehandle = open("/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/PythonNotes.txt", 'w')
# Further notes of file operations:
# r opens the file for read only
# r+ opens for read and write
# w opens for write only
# w+ opens a file for both write and read
# a opens for appending
# a+ opens for append and read


# filehandle = open("/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/PythonNotes.txt", 'a')
# filehandle.write("Hello from python!!!\n")
# mylist = ['foo','bar','fart','barf','fleebaz']
# for x in mylist:
#     filehandle.write(x + "\n")
# filehandle.close()


# The with statement:
with open("/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/PythonNotes.txt", 'a+') as filehandle:
    filehandle.write("This is the with statement!!!\n")
    filehandle.seek(0)
    content = filehandle.readlines()
    for x in content:
        print(x)
        

    



