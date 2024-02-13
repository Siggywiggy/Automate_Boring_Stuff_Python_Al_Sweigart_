#! python3
# a program that opens 10 first product sites on amazon

import bs4
import requests
import sys
import webbrowser

print("Searching for products...")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
}
res = requests.get(
    "https://www.amazon.de/s?k=" + " ".join(sys.argv[1:]), headers=headers
)

# check if download went OK
try:
    res.raise_for_status()
except Exception as err:
    print(f"Something went wrong with the download.. {err}")
# create bs4 object and parse it with lxml parser
soup = bs4.BeautifulSoup(res.text, "lxml")

# select all items that seem to be links
link_elements = soup.select("a-link-normal a-text-normal")

print(f"found {len(link_elements)} links in total!")

# define how many links to open
num_open = min(5, len(link_elements))

for i in range(num_open):
    print(f'link {i} is {link_elements[i].get("href")}')
    url_to_open = "https://www.amazon.de/s?k=" + link_elements[i].get("href")
    webbrowser.open(url_to_open)
