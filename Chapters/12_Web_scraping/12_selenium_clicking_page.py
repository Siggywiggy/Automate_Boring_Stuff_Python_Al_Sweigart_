from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    link_element = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
except Exception as err:
    print(f'something went wrong: {err}')

print(type(link_element))

link_element.click()