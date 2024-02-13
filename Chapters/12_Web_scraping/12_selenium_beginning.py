from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element(By.CLASS_NAME, 'card-img-top ')
    print(f'found {elem.tag_name} with that class name (card-img-top)')
except Exception as err:
    print(f'something went wrong: {err}')