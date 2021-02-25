import os
# opening statement
print("put file here")
#inputs user input into program
path = os.path.abspath(input())
size = 0
# folder path input
print("Enter folder path")
path = os.path.abspath('C:\Program Files\Common Files')

# for storing size of each file
size = 0

# for storing the size of the largest file
max_size = 0

# for storing the path to the largest file
max_file = ""

# for storing the name of the largest file
file_name = ""

# walking through the entire folder, including subdirectories

for folder, subfolders, files in os.walk(path):
    for file in files:
        size = os.stat(os.path.join(folder,file)).st_size

        if size>max_size:
            max_size = size
            name = folder + file

print("the largest file is: "+name)
print('Size: '+str(max_size)+' bytes')