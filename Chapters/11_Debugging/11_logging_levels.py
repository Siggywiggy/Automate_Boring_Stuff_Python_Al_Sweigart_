"""DEBUG - logging.debug() - The lowest level. 
Used for small details. Usually you care about these messages only when diagnosing problems."""

"""INFO - logging.info() - Used to record information on general events in your program 
or confirm that things are working at their point in the program.
"""

"""WARNING - logging.warning() - Used to indicate a potential problem that doesn’t
 prevent the program from working but might do so in the future."""

"""ERROR - logging.error() - Used to record an error 
that caused the program to fail to do something."""

""" CRITICAL - logging.critical() - The highest level. Used to indicate
a fatal error that has caused or is about to cause the program to stop running entirely."""

import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s -  %(message)s"
)

logging.debug("Some debugging details.")
logging.info("The logging module is working.")
logging.warning("An error message is about to be logged.")
logging.error("An error has occurred.")
logging.critical("The program is unable to recover!")
