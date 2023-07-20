import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pickle
import csv
from fake_useragent import UserAgent
from pass_var import *
from art import tprint

url = [
    'https://stavropol.hh.ru/search/resume?text=&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&exp_industry=any&area=84&relocation=living_or_relocation&salary_from=&salary_to=&currency_code=RUR&age_from=&age_to=&gender=unknown&order_by=relevance&search_period=0&items_on_page=50',
    'https://trudvsem.ru/cv/search?_regionIds=2600000000000&page=0&salary=0&salary=999999&experience=EXP_STAFF&cvType=LONG',
    'https://www.avito.ru/moskva/rezume',
    'https://joblab.ru/access.php',
    'https://www.rabota.ru/v3_login.html'
    'https://gorodrabot.ru/site/login',

]

project = []


u_ag = UserAgent()
agent = u_ag.random
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent{agent}')
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
# options.set_preference("dom.webdriver.enabled", False)
print(agent)


def get_cookies():
    # # try:
    # #     driver.get(url[0])
    # #     # form = driver.find_element(By.CLASS_NAME, 'account-login-tile')
    # # # time.sleep(1)
    # # # button_dop = form.find_element(By.CLASS_NAME, 'bloko-link_pseudo')
    # # # time.sleep(1)
    # # # button_dop.click()
    # # # time.sleep(2)
    # # # input_dop = driver.find_elements(By.CLASS_NAME, 'bloko-input-text')
    # # # print(len(input_dop))
    # # # time.sleep(5)
    # # # input_dop[1].send_keys(login)
    # # # time.sleep(4)
    # # # input_dop[2].send_keys(passwords)
    # # # time.sleep(3)
    # # # input_dop[2].send_keys(Keys.ENTER)
    # # # time.sleep(40)
    # # # pickle.dump(driver.get_cookies(), open('cookies_hh_ru', 'wb'))
    # #     time.sleep(2)
    # #     cookie = pickle.load(open('cookies_hh_ru', 'rb'))
    # #     for cookie in pickle.load(open('cookies_hh_ru', 'rb')):
    # #         driver.add_cookie(cookie)
    # #     time.sleep(2)
    # #     driver.refresh()
    # #     time.sleep(10)
    # # except Exception as ex:
    # #     print(ex)
    # #     driver.quit()
    # #     driver.close()
    # # finally:
    # #     print("Куки успешно загружены = ", url[0])
    #
    # try:
    #     driver.get(url[1])
    #     time.sleep(2)
    #     div_load = driver.find_element(By.CLASS_NAME, 'main__search-sidebar')
    #     time.sleep(2)
    #     button_load = div_load.find_elements(By.TAG_NAME, 'button')
    #     time.sleep(3)
    #     while len(button_load) == 1:
    #         print('Кнопка есть  = ', len(button_load))
    #         humans = driver.find_elements(By.CLASS_NAME, 'search-results-simple-card')
    #         if len(humans) >= 350:
    #             print('Кнопка нет  = ', len(button_load))
    #             break
    #         print('Найдено соискателей = ', len(humans))
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         time.sleep(2)
    #         button_load = div_load.find_elements(By.TAG_NAME, 'button')
    #         button_load[0].click()
    #         time.sleep(2)
    #     print('---------------------------------------------------------------------------------------------')
    #         # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         # time.sleep(3)
    #         # humans = driver.find_elements(By.CLASS_NAME, 'search-results-simple-card')
    #     page = driver.page_source
    #     page_hh_ru = BeautifulSoup(page, 'html.parser')
    #     with open("trudvsem.html", "w", encoding="utf-8") as file:
    #         file.write(page_hh_ru.prettify())
    #     time.sleep(10)
    #     humans_bs = page_hh_ru.find_all('div', {'class': 'search-results-simple-card__main-content search-results-simple-card__name'})
    #     for human in humans_bs:
    #         project.append({
    #             'title': human.text,
    #         })
    #
    #
    #
    #
    # except Exception as ex:
    #     print(ex)
    #     driver.quit()
    #     driver.close()
    # finally:
    #     print("Куки успешно загружены = ", url[1])
    #     for job in project:
    #         print(job.text)

    try:
        driver.get(url[2])
        time.sleep(4)
        # time.sleep(10)
        # button_login = driver.find_element(By.CSS_SELECTOR, '.index-inner-iPEdy > a')
        # time.sleep(1)
        # # #login?authsrc=h
        # button_login.click()
        # time.sleep(10)
        # form = driver.find_element(By.CSS_SELECTOR, '.AuthorizationMainScreen-content-ssDk6 > form')
        # input_value = form.find_elements(By.TAG_NAME, 'input')
        # time.sleep(3)
        # print(len(input_value))
        # input_value[0].send_keys(login_avito)
        # time.sleep(1)
        # input_value[1].send_keys(password_avito)
        # time.sleep(3)
        # input_value[1].send_keys(Keys.ENTER)
        # time.sleep(300)
        # pickle.dump(driver.get_cookies(), open('cookies_avito', 'wb'))
        # time.sleep(2)
        page = driver.page_source
        page_soup_bs = BeautifulSoup(page, 'html.parser')
        cookie = pickle.load(open('cookies_avito', 'rb'))
        for cookie in pickle.load(open('cookies_avito', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(2)
        driver.refresh()
        time.sleep(10)
    except Exception as ex:
        print(ex)

    finally:
        print("Куки успешно загружены = ", url[2])

    return (page_soup_bs)
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


def parse_avito(data):
    tprint("Parser_Avito")
    time.sleep(3.5)
    page_max = data.find('div', {'class': 'js-pages pagination-pagination-_FSNE'}).find_all('span', {'class': 'styles-module-text-InivV'})
    int_max_page = int(page_max[6].get_text())
    print('Максимальное кол-во станиц = ', int_max_page)

    for i in range(int_max_page):
        url_next = url[2] + f'?p={i}'
        driver.get(url_next)
        for cookie in pickle.load(open('cookies_avito', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(3)
        catalog = data.find('div', {'class': 'items-items-kAJAg'})
        card_all = catalog.find_all('div', {'class': 'iva-item-body-KLUuy'})



        for card in card_all:
            i = 0

            p = card.find_all('p')
            print(len(p))
            # card_text = card.find('div', {'class': 'iva-item-descriptionStep-C0ty1'})
            i = i + 1

            project.append({
                'name': card.find('h3', {'class': 'styles-module-root-TWVKW styles-module-root-_KFFt styles-module-size_l-_oGDF styles-module-size_l-hruVE styles-module-ellipsis-LKWy3 styles-module-weight_bold-Kpd5F stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-header-l-qvNIS'}).text,
                'ZP': card.find('span', {'class': ''}).text,
                'gender/time_jobs': card.find('span', {'class': 'styles-module-noAccent-nZxz7 styles-module-size_s-awPvv'}).get_text(),
                'description': p[i].text,
                # 'time_publication': p[y].text,
            })

        for project_ in project:
            print(project_)
        print('Найдена карточек всего на этом сайте = ', len(project), url_next)

def main():
    parse_avito(get_cookies())


if __name__ == '__main__':
    main()