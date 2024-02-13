from pathlib import Path

print(Path.cwd())
spam_path_obj = Path("spam.txt")

# writes text in to the file referred by Path object
spam_path_obj.write_text("Hello, world!")
print(spam_path_obj.read_text())

# open file with open() function - returns a File object

hello_file = open(Path.cwd() / "hello.txt")

hello_file = open(
    "/home/aadamkurm/Documents/Programmeerimine/Automate_boring_stuff_Python/new_run/9_Reading_writing_files/spam.txt"
)

# using read method on File object to read its contents
hello_file_content = hello_file.read()
print(hello_file_content)
hello_file.close()

# getting a list of strings with readlines() method, returns a list of strings!
sonnet_file = open(Path.cwd() / "sonnet29.txt")
print(sonnet_file.readlines())
sonnet_file.close()
# writing to files
# write mode will overwrite, append will append to the end of the existing text

bacon_file = open("bacon.txt", "w")
bacon_file.write("Hello, world!\n")
bacon_file.close()
bacon_file = open("bacon.txt", "a")
bacon_file.write("Bacon is not a vegetable!")
bacon_file.close()
bacon_file = open("bacon.txt", "r")
content = bacon_file.readlines()
bacon_file.close()
print(content)
