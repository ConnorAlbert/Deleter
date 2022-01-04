import os
import shutil


def Delete_Files():
    os.chdir(r"Your directory here")  # Current location
    directory = r'Your directory here'
    for filename in os.listdir(directory):  # list files in directory
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            delete = filename
            print(f)

    src = f  # Move from current location
    dst = r"Directory to move file"  # Move to location

    print("Press Enter to delete and n to move: ")
    file = input(f'Do you want to delete:{delete} ')
    if file == '':
        print('\nStarting the removal of the file !')
        os.remove(delete)
        print('\nFile, ', delete,
              'The file deletion is successfully completed !!\n')
        Delete_Files()
    elif file == "n":
        if os.path.isdir(dst+'/'+delete):
            print(delete, 'exists in the destination path!')
            shutil.rmtree(dst+'/'+delete)
        elif os.path.isfile(dst+'/'+delete):
            os.remove(dst+'/'+delete)
            print(delete, 'deleted in', dst)
        dest = shutil.move(src, dst)
    Delete_Files()


Delete_Files()
