#! python3
# a program that opens 5 first search results of gogle search from command line arg keywords

import bs4
import requests
import sys
import webbrowser

# Read command line arguments from sys.argv
print("Searching......")
# fetch search result page with the requests module
# "https://google.com/search?q="
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
# check if the download went OK
try:
    res.raise_for_status()
except Exception as exc:
    print(f"there was a problem {exc}")

# find the links to each search result
soup = bs4.BeautifulSoup(res.text, "lxml")  # use bs4 to parse the HTML with lxml parser
link_elements = soup.select(
    ".package-snippet"
)  # select all elements that sem to be the links
print(f"found {len(link_elements)} links in total!")
# print(link_elements[1])
# call webbrowser.open(function) on all result links to open the web broser
num_open = min(
    5, len(link_elements)
)  # will open either 5 or how many links were found, the smallest of the two

# print(link_elements[0].get("href"))

for i in range(num_open):
    url_to_open = "https://pypi.org" + link_elements[i].get("href")
    webbrowser.open(url_to_open)
