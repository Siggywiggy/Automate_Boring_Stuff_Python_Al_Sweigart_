#! python3
# a program that opens 10 result links in web browser after imgur search

import bs4
import requests
import sys
import webbrowser

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
}


print(f"Searching for pictures with keyword {str(sys.argv[1:])}")

request_object = requests.get(
    "https://imgur.com/search?q=" + " ".join(sys.argv[1:]),
    headers=headers,
)

try:
    request_object.raise_for_status()
except Exception as err:
    print(f"Something went wrong with download! {err}")

soup_object = bs4.BeautifulSoup(request_object.text, "lxml")
link_elements = soup_object.select(".image-list-link")
print(f"found {len(link_elements)} links in total!")

for i in range(min(10, len(link_elements))):
    url_suffix = link_elements[i].get("href")
    webbrowser.open("imgur.com" + url_suffix)
