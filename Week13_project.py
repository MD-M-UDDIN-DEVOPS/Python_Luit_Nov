import os

# Get the list of files in the current working directory

file_list = os.listdir(os.getcwd())

# Initialize an empty list to store the file information

file_info = []

# Iterate over the list of files

for file in file_list:
    
    # Get the file size in bytes
    
    file_size = os.stat(file).st_size

    # Add the file information to the list as a dictionary
    
    file_info.append({
        'name': file,
        'size': file_size
    })

# Print the list of file information

# print(file_info)

print(*file_info, sep ="\n")