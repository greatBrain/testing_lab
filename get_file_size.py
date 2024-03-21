import os

file = "file.txt"

def get_file_size():
    global file
    return os.path.getsize(file) == 0

print(get_file_size())
