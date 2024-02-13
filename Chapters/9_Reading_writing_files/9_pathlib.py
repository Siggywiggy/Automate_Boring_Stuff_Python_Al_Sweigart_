from pathlib import Path

# prints \ dividers for windows system (WindowsPath objecty) and / dividers for unix paths (PosixPath objects)

print(str(Path("spam", "bacon", "eggs")))

my_files = ["accounts.txt", "details.csv", "invite.docx"]
for filename in my_files:
    print(Path(r"C:/Users/Al", filename))
