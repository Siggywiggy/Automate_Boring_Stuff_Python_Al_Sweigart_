from pathlib import Path

# p.exists() returns True if the path exists or returns False if it doesn’t exist.
# p.is_file() returns True if the path exists and is a file, or returns False otherwise.
# Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.


linux_dir = Path("/usr/bin/")

not_existant_dir = Path("/home/usr/My_Documents")

arduino_project_file = Path(
    "/home/aadamkurm/Documents/IoT_projects/Arduino/Hello_World.ino/helloworld_sketch/helloworld_sketch.ino"
)

print(linux_dir.exists())
print(not_existant_dir.exists())
print(arduino_project_file.is_file())
print(arduino_project_file.is_dir())

# check if DVD of flash drive is currently attached to the computer

secondary_drive = Path("/run/media/aadamkurm/Old Windows")

print("check if Old Windows drive is mounted:")
print(secondary_drive.exists())

flash_drive = Path("/run/media/aadamkurm/USB_util")
print("check if USB drive is mounted:")
print(flash_drive.exists())
