from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('')

try:
    user_name_element = browser.find_element(By.ID, 'email')
except Exception as err:
    print(f'something went wrong: {err}')

user_name_element.send_keys('')

try:
    password_element = browser.find_element(By.ID, 'password')
except Exception as err:
    print(f'something went wrong: {err}')

password_element.send_keys('')

log_in_button = browser.find_element(By.CLASS_NAME, 'btn')
log_in_button.click()

