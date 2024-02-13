import bs4

example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file.read(), "lxml")
elements = example_soup.select("#author")
print(type(elements))
print(len(elements))
print(type(elements[0]))
print(str(elements[0]))
element_content = elements[0].getText()
print(element_content)
print(elements[0].attrs)

p_elements = example_soup.select("p")
print(f"found {len(p_elements)} <p> elements in the HTML response")
print(str(p_elements[0]))
print(p_elements[0].getText())
print(str(p_elements[1]))
print(p_elements[1].getText())
print(str(p_elements[2]))
print(p_elements[2].getText())
example_file.close()

# css selector copy
#"""div.row-odd:nth-child(1) > div:nth-child(2)"""