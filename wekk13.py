import os

# Get current working directory
file_path = os.getcwd()

# List to store file information
file_list = []

# Loop through the files in the current working directory
for filename in os.listdir(file_path):
    file_path = os.path.join(file_path, filename)
    if os.path.isfile(file_path):
        file_info = {
            "name": filename,
            "size": os.path.getsize(file_path)
        }
        file_list.append(file_info)

# Print the list of dictionaries
print(*file_list, sep="\n")
