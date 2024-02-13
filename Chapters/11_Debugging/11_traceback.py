import traceback

try:
    raise Exception("This is the error message")
except:
    errorFile = open("errorInfo.txt", "w")
    errorFile.write(traceback.format_exc())  # obtains the exception as a string
    errorFile.close()
    print("The traceback info was written to errorInfo.txt.")
