#! python3
# map_it.pyu - program that opens google maps location with command line args or clipboard
# https://www.google.com/maps/place/Kadaka+pst+165c,+11625+Tallinn/

import pyperclip
import sys
import webbrowser

# address_string = "https://www.google.com/maps/place/Kadaka+pst+165c,+11625+Tallinn/"

# webbrowser.open(address_string)

# sys.argv stores a list of filename + command line arguments
# if this list has more then filename, it means command line arguments have been provides

if len(sys.argv) > 1:
    # Get address from command line
    address = " ".join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
