#importing function/method
import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*') #this matches all file's and directories in the home directory

file_list = glob.glob(pattern) #retrieves all file and directories names matching the pattern

for file in file_list:
    file_size = os.path.getsize(file) #gets file size in bytes

    if file_size > 0: # checks if the file is not empty
        file_name = os.path.basename(file) #gets just the file name without the file path
        print(f"{file_name} - {file_size} bytes") # prints the file name and size using an 'f' string

        change test git