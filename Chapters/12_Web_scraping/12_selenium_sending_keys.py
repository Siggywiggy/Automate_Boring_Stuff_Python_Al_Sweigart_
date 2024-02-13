from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('https://nostarch.com')

try:
    html_element = browser.find_element(By.TAG_NAME, 'html')
except Exception as err:
    print(f'something went wrong: {err}')

html_element.send_keys(Keys.END)
time.sleep(2)
html_element.send_keys(Keys.HOME)
