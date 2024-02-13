#! Python 3
# a program that takes an email address and string of text from command line
# logs in to email account and send and email of the string to the provided address

# programs email account = adam783t86725t6
# email eccount password = Zc?PrN4w3v4FiD:

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


if len(sys.argv) > 0:
    print('command line arguments seen')

target_email = sys.argv[1]
message = sys.argv[2]

browser = webdriver.Firefox()
browser.get('https://www.mail.ee/')

try:
    user_name_element = browser.find_element(By.ID, 'imapuser')
except Exception as err:
    print(f'something went wrong: {err}')

user_name_element.send_keys('adam783t86725t6')

try:
    password_element = browser.find_element(By.ID, 'pass')
except Exception as err:
    print(f'something went wrong: {err}')

password_element.send_keys('Zc?PrN4w3v4FiD:')

password_element.submit()

time.sleep(5)
try:
    new_email_button = browser.find_element(By.CLASS_NAME, 'Text-sc-q3cmx5-2')
except Exception as err:
    print(f'something went wrong: {err}')

new_email_button.click()

try:
    to_field = browser.find_element(By.ID, 'suggest-to')
except Exception as err:
    print(f'something went wrong: {err}')

to_field.send_keys(target_email)

try:
    subject_field = browser.find_element(By.ID, 'subject')
except Exception as err:
    print(f'something went wrong: {err}')

subject_field.send_keys('test email')

try:
    content_field = browser.find_element(By.ID, 'cke_eml-compose__message')
except Exception as err:
    print(f'something went wrong: {err}')

ActionChains(browser).move_to_element(content_field).click(content_field).send_keys('lorem ipsum dolor sit amet').perform()
#content_field.send_keys('lorem ipsum dolor sit amet')

try:
    send_button = browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/table/tbody/tr/td[2]/div/div[1]/button[2]')
except Exception as err:
    print(f'something went wrong: {err}')

send_button.click()