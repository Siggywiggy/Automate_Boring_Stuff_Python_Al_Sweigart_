import os

# os.path.getsize(path) will return the size in bytes of the file in the path argument.
# os.listdir(path) will return a list of filename strings for each file in the path argument.

print(
    os.path.getsize(
        "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files/9_os_path_module.py"
    )
)

print(
    os.listdir(
        "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files"
    )
)

total_size = 0

for filename in os.listdir(
    "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files"
):
    total_size += os.path.getsize(
        os.path.join(
            "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files",
            filename,
        )
    )

print(f"The total size of the folder is {total_size} bytes.")
