__author__ = 'Sergey'

import shutil
import os
import stat


def read_all_directory_path(root_folder, final_directory_list=[], folder_for_remove='.svn'):
    under_files_and_folders = os.listdir(root_folder)

    if os.path.split(root_folder)[1] == folder_for_remove:
        final_directory_list.append(root_folder)
        return final_directory_list

    if len(under_files_and_folders) == 0:
        final_directory_list.append(root_folder)
        return final_directory_list

    for dir in under_files_and_folders:
        sub_path = root_folder + "\\" + dir
        if os.path.isfile(sub_path):
            continue
        read_all_directory_path(sub_path, final_directory_list)


def change_file_attributes_in_folder(folder):
    list_files_and_directories = os.listdir(folder)

    for item in list_files_and_directories:
        sub_path = folder + "\\" + item
        if os.path.isfile(sub_path):
            os.chmod(sub_path, stat.S_IWRITE)
            os.unlink(sub_path)
        else:
            change_file_attributes_in_folder(sub_path)


directory_list = []
root = "D:\\_svn_repo\\trunk"
remove_dir = ".svn"

# 1 - read all directories recursively and store to a variable list of directory.
read_all_directory_path(root, directory_list)

# 2 - remove directory from the variable.
for directory in directory_list:
    if os.path.split(directory)[1] == remove_dir:
        try:
            shutil.rmtree(directory)
        except WindowsError, e:
            if "Access is denied" in e.strerror:
                change_file_attributes_in_folder(directory)
                shutil.rmtree(directory)
            else:
                raise
