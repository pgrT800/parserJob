import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pickle
import csv
from pass_var import passwords, login

hh_ru_url = 'https://stavropol.hh.ru/account/login?backurl=%2F&hhtmFrom=account_login'

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()

try:
    driver.get(hh_ru_url)

    # form = driver.find_element(By.CLASS_NAME, 'account-login-tile')
    # time.sleep(1)
    # button_dop = form.find_element(By.CLASS_NAME, 'bloko-link_pseudo')
    # time.sleep(1)
    # button_dop.click()
    # time.sleep(2)
    # input_dop = driver.find_elements(By.CLASS_NAME, 'bloko-input-text')
    # print(len(input_dop))
    # time.sleep(5)
    # input_dop[1].send_keys(login)
    # time.sleep(4)
    # input_dop[2].send_keys(passwords)
    # time.sleep(3)
    # input_dop[2].send_keys(Keys.ENTER)
    # # parserparser228
    # time.sleep(40)
    # pickle.dump(driver.get_cookies(), open('cookies_hh_ru', 'wb'))
    time.sleep(10)

    cookie = pickle.load(open('cookies_hh_ru', 'rb'))
    for cookie in pickle.load(open('cookies_hh_ru', 'rb')):
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    time.sleep(15)


except Exception as ex:
    print(ex)
finally:
    driver.quit()
    driver.close()
