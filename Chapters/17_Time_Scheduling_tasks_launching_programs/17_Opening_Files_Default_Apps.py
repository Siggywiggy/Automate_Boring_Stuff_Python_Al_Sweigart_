# Windows = start program
# Ubuntu Linux = see program
import subprocess

file_object = open("hello.txt", "a")
file_object.write("second row! \n")
file_object.close()

subprocess.Popen(["start", "hello.txt"], shell=True)
