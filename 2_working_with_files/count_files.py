import os.path


# Counting only regular files (not folders)
path = "example_files/text_files"
number_files = len([file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))])
print(f"There are {number_files} regular files in directory: {path}")
