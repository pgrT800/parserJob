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

url =[
 'https://stavropol.hh.ru/search/resume?text=&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&exp_industry=any&area=84&relocation=living_or_relocation&salary_from=&salary_to=&currency_code=RUR&age_from=&age_to=&gender=unknown&order_by=relevance&search_period=0&items_on_page=50',
 'https://trudvsem.ru/cv/search?_regionIds=2600000000000&page=0&salary=0&salary=999999&experience=EXP_STAFF&cvType=LONG',
 'https://www.avito.ru/moskva/rezume'  
 'https://joblab.ru/access.php',
 'https://www.rabota.ru/v3_login.html'
 'https://gorodrabot.ru/site/login',
]

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
project = []

def get_cookies():
    # try:
    #     driver.get(url[0])
    #     # form = driver.find_element(By.CLASS_NAME, 'account-login-tile')
    # # time.sleep(1)
    # # button_dop = form.find_element(By.CLASS_NAME, 'bloko-link_pseudo')
    # # time.sleep(1)
    # # button_dop.click()
    # # time.sleep(2)
    # # input_dop = driver.find_elements(By.CLASS_NAME, 'bloko-input-text')
    # # print(len(input_dop))
    # # time.sleep(5)
    # # input_dop[1].send_keys(login)
    # # time.sleep(4)
    # # input_dop[2].send_keys(passwords)
    # # time.sleep(3)
    # # input_dop[2].send_keys(Keys.ENTER)
    # # time.sleep(40)
    # # pickle.dump(driver.get_cookies(), open('cookies_hh_ru', 'wb'))
    #     time.sleep(2)
    #     cookie = pickle.load(open('cookies_hh_ru', 'rb'))
    #     for cookie in pickle.load(open('cookies_hh_ru', 'rb')):
    #         driver.add_cookie(cookie)
    #     time.sleep(2)
    #     driver.refresh()
    #     time.sleep(10)
    # except Exception as ex:
    #     print(ex)
    #     driver.quit()
    #     driver.close()
    # finally:
    #     print("Куки успешно загружены = ", url[0])

    try:
        driver.get(url[1])
        time.sleep(2)
        div_load = driver.find_element(By.CLASS_NAME, 'main__search-sidebar')
        time.sleep(2)
        button_load = div_load.find_elements(By.TAG_NAME, 'button')
        time.sleep(3)
        while len(button_load) == 1:
            print('Кнопка есть  = ', len(button_load))
            humans = driver.find_elements(By.CLASS_NAME, 'search-results-simple-card')
            if len(humans) >= 340:
                print('Кнопка нет  = ', len(button_load))
                break
            print('Найдено соискателей = ', len(humans))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            button_load = div_load.find_elements(By.TAG_NAME, 'button')
            button_load[0].click()
            time.sleep(2)
        print('---------------------------------------------------------------------------------------------')
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(3)
            # humans = driver.find_elements(By.CLASS_NAME, 'search-results-simple-card')
        page = driver.page_source
        page_hh_ru = BeautifulSoup(page, 'html.parser')
        with open("trudvsem.html", "w", encoding="utf-8") as file:
            file.write(page_hh_ru.prettify())
        time.sleep(10)
        humans_bs = page_hh_ru.find_all('div', {'class': 'search-results-simple-card__main-content search-results-simple-card__name'})
        for human in humans_bs:
            project.append({
                'title': human.text,
            })



    except Exception as ex:
        print(ex)
        driver.quit()
        driver.close()
    finally:
        print("Куки успешно загружены = ", url[1])
        for job in project:
            print(project)

    # try:
    #     driver.get(url[2])
    #     time.sleep(2)
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     print("Куки успешно загружены = ", url[2])
    #
    # try:
    #     driver.get(url[3])
    #     time.sleep(2)
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     print("Куки успешно загружены = ", url[3])
    #
    # try:
    #     driver.get(url[4])
    #     time.sleep(2)
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     print("Куки успешно загружены = ", url[4])
    #
    # try:
    #     driver.get(url[5])
    #     time.sleep(2)
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     print("Куки успешно загружены = ", url[5])




def main():
    get_cookies()


if __name__ == '__main__':
    main()