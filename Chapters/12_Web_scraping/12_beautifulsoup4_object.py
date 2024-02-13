import requests
import bs4

res = requests.get("https://nostarch.com")
# checking is there were any errors

try:
    res.raise_for_status()
except Exception as exc:
    print(f"There was a problem: {exc}")

no_starch_soup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(no_starch_soup))

# loading HTML file from HDD
example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file, "html.parser")
print(type(example_soup))

# a faster parser is lxml
example_soup = bs4.BeautifulSoup(example_file, "lxml")
print(type(example_soup))
