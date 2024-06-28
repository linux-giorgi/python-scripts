import os
import shutil

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def sort_files_by_extension(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1][1:]  # Get the file extension without the dot
            if file_extension:  # Check if there is an extension
                folder_path = os.path.join(directory, file_extension)
                create_folder(folder_path)
                shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))
            else:
                # Files without an extension
                no_ext_folder = os.path.join(directory, "no_extension")
                create_folder(no_ext_folder)
                shutil.move(os.path.join(directory, filename), os.path.join(no_ext_folder, filename))

if __name__ == "__main__":
    directory = input("Enter the path of the directory to sort: ")
    if os.path.exists(directory):
        sort_files_by_extension(directory)
        print(f"Files in '{directory}' have been sorted by their extensions.")
    else:
        print("The specified directory does not exist.")
