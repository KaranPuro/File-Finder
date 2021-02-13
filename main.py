import os


# folder path input
print("Enter folder path")
path = os.path.abspath('C:\Program Files\Common Files')

# for storing size of each file
size = 0

# for storing the size of the largest file
max_size = 0

# for storing the path to the largest file
max_file = ""

# walking through the entire folder, including subdirectories

for folder, subfolders, files in os.walk(path)
    for file in files:
        size = os.stat(os.path.join('C:\Program Files\Common Files')).st_size

        if size>max_size:
            max_size = size

print("the largest file is: "+max_file)
print('Size: '+str(max_size)+' bytes')