import bs4

soup = bs4.BeautifulSoup(open("example.html"), "lxml")
span_element_1 = soup.select("span")[0]
print(str(span_element_1))
span_element_1.get("id")
print(span_element_1.get("some_non_existant_addr") == None)
print(span_element_1.attrs)
