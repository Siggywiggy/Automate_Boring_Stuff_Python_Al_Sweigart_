#! python3
# Copies an entire folder and its contents into a Zip file whose filename increments

import os, zipfile


def back_up_to_zip(folder):
    # back up th e entire content of "folder" into a ZIP file
    folder = os.path.abspath(folder)  # making sure folder is absolute path
    # figure out filename this code should use based on what files already exist
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_file_name):
            break
        number += 1

    # create the ZIP file
    print(f"Creating {zip_file_name}...")
    back_up_zip = zipfile.ZipFile(zip_file_name, "w")
    # walk the entire folder and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")
        # add the current folder to the ZIP file
        back_up_zip.write(foldername)
        # add all the files in this folder to the ZIP file
        for file_name in filenames:
            new_base = os.path.basename(folder) + "_"
            if file_name.startswith(new_base) and file_name.endswith(".zip"):
                continue  # dont back up the backup ZIP files
            back_up_zip.write(os.path.join(foldername, file_name))

    back_up_zip.close()

    print("Done")


back_up_to_zip(
    "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/10_Organizing_files"
)
