import zipfile

new_zip = zipfile.ZipFile("new.zip", "w")
new_zip.write("spam.txt", compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()

new_zip = zipfile.ZipFile("new.zip")
print(new_zip.namelist())
spam_info = new_zip.getinfo("spam.txt")
print(spam_info.file_size)
print(spam_info.compress_size)
new_zip.close()
