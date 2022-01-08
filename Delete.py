import os
import shutil

def main():
    rawdirectory = input("Enter directory here: ")  # Current location
    directory = rawdirectory.strip(' " " ')
    rawdst = input("Enter location to move file or leave blank to skip: ")  # Move to location
    dst = rawdst.strip(' " " ')
    start(directory, dst)

def start(directory, dst):
    os.chdir(directory)
    dir = os.listdir(directory)

    # Checking if the list is empty or not
    if len(dir) == 0:
        print("Directory is empty goodbye")
        exit()

    print("\nlist of files/folders")
    print("------------------")
    for myfiles in os.listdir(directory):  # list files in directory
        File_Folder = os.path.join(myfiles)
        if os.path.isdir(File_Folder) or os.path.isfile(File_Folder):
            print(File_Folder)

    move = File_Folder

    print("------------------")
    print("\nPress Enter to delete and m to move: ")
    file = input(f'Do you want to delete: {File_Folder} ??? ')
    if file == '':
        print('\nStarting the removal of the file !')
        try:
            os.remove(File_Folder)
            start(directory, dst)
        except PermissionError:
            shutil.rmtree(File_Folder)
            start(directory, dst)
        print('\nFile, ', File_Folder,
              'The file deletion is successfully completed !!\n')

    elif file == "m":
        try:
            dest = shutil.move(move, dst)
        except shutil.Error as err:
            if os.path.isdir(dst+'/'+File_Folder):
                print(File_Folder, 'exists in the destination path!')
                shutil.rmtree(dst+'/'+File_Folder)
                print(File_Folder, 'deleted in', dst)
            elif os.path.isfile(dst+'/'+File_Folder):
                print(File_Folder, 'exists in the destination path!')
                os.remove(dst+'/'+File_Folder)
                print(File_Folder, 'deleted in', dst)
            dest = shutil.move(move, dst)

    else:
        main()
main()
