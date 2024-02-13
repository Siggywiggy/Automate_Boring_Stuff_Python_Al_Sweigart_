import logging

logging.basicConfig(
    filename="myProgramLog.txt",  # filename argument lets you specify filename to write log in to
    level=logging.DEBUG,
    format=" %(asctime)s -  %(levelname)s -  %(message)s",
)
