import os

def remove_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to remove '{file_name}'.")

if __name__ == "__main__":
    file_names = ["file.txt.lzw", "file.txt.2", "file.txt.lzw2", "file.txt.2M"]
    for file in file_names:
        remove_file(file)
