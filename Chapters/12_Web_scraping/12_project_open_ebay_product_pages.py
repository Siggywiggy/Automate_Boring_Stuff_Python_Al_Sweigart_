#! python3
# a program that opens 5 first search results on ebay
# gets the product name, price and top feedback comment
# writes results to a txt file

import bs4
import requests
import sys

print("Searching for products...")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
}
res = requests.get(
    "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw="
    + " ".join(sys.argv[1:])
    + "&_sacat=0",
    headers=headers,
)

# check if download went OK
try:
    res.raise_for_status()
except Exception as err:
    print(f"Something went wrong with the download.. {err}")
# create bs4 object and parse it with lxml parser
soup = bs4.BeautifulSoup(res.text, "lxml")

# select all items that seem to be links
link_elements = soup.select(".s-item__link")

print(f"found {len(link_elements)} links in total!")

# define how many links to open
num_open = min(6, len(link_elements))

summary_dict = {}

for i in range(1, num_open):
    product_summary = []
    url_to_open = link_elements[i].get("href")
    request_object = requests.get(url_to_open, headers=headers)
    try:
        request_object.raise_for_status()
    except Exception as err:
        print(f"Something went wrong with the download: {err}")

    beautiful_soup_object = bs4.BeautifulSoup(request_object.text, "lxml")
    #product_name_element = beautiful_soup_object.select(".x-item-title__mainTitle")
    product_name_element = beautiful_soup_object.select('.x-item-title__mainTitle > span:nth-child(1)')
    price_element = beautiful_soup_object.select('.x-price-primary > span:nth-child(1)')
    #price_element = beautiful_soup_object.select(".x-price-primary .ux-textspans")
    top_feedback_element = beautiful_soup_object.select(
        ".fdbk-container__details__comment"
    )
    product_name_result = product_name_element[0].getText()
    product_summary.append(product_name_result)
    price_result = price_element[0].getText()
    product_summary.append(price_result)
    top_feedback_element_result = top_feedback_element[0].getText()
    product_summary.append(top_feedback_element_result)
    #print(f"the name of the product is {product_name_result}")
    # print(f"The price of the product is {price_result}")
    # print(f'The top feedback comment is \n "{top_feedback_element_result}"')
    # print("\n")
    summary_dict[f"product{i}"] = product_summary

summary_file = open("summary.txt", "a", encoding="utf-8")

for key, value_list in summary_dict.items():
    summary_file.write(f"{str(key)}")
    for value in value_list:
        # print(f"{str(value)} \n")
        summary_file.write(f"{str(value)}" + " - ")
    summary_file.write("\n")

summary_file.close()
