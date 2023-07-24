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
    'https://stavropol.hh.ru/search/resume',
    'https://trudvsem.ru/cv/search?_regionIds=2600000000000&page=0&salary=0&salary=999999&experience=EXP_STAFF&cvType=LONG',
    'https://www.avito.ru/moskva/rezume',
    'https://joblab.ru/access.php',
    'https://www.rabota.ru/v3_login.html'
    'https://gorodrabot.ru/site/login',
]

project = []

u_ag = UserAgent()
agent = u_ag.random
options = webdriver.EdgeOptions()
options.add_argument(f'user-agent{agent}')
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Edge(options=options)
# options.set_preference("dom.webdriver.enabled", False)
print(agent)


def get_cookies_hh_ru():
    # Куки хх ру и возвращение обьекта bs4
    try:
        driver.get(url[0])
        time.sleep(4)
        page_hh_ru = driver.page_source
        page_soup_hhru = BeautifulSoup(page_hh_ru, 'html.parser')
        for cookie in pickle.load(open('cookies_hh_ru', 'rb')):
            driver.add_cookie(cookie)

        time.sleep(2)
        driver.refresh()
        time.sleep(6)
    except Exception as ex:
        print(ex)

    finally:
        print("Куки хх ру успешно загружены = ", url[0])

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
    # Подгрузка куки Авито

    return page_soup_hhru


def get_cookies_avito():
    # Подгрузка куки авито и возвращение обьекта bs4
    try:
        driver.get(url[2])
        time.sleep(4)
        page = driver.page_source
        page_soup_avito = BeautifulSoup(page, 'html.parser')
        for cookie in pickle.load(open('cookies_avito', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(2)
        driver.refresh()
        time.sleep(10)
    except Exception as ex:
        print(ex)

    finally:
        print("Куки авито успешно загружены = ", url[2])

    return page_soup_avito
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


def parse_avito(page_soup_avito):
    tprint("Parser_Avito")
    time.sleep(6)
    page_max = page_soup_avito.find('div', {'class': 'js-pages pagination-pagination-_FSNE'}).find_all('span', {'class': 'styles-module-text-InivV'})
    int_max_page = int(page_max[6].get_text())
    print('Максимальное кол-во станиц = ', int_max_page)
    i = 2
    for i in range(4):
        url_next = url[2] + f'?p={i}'
        driver.get(url_next)
        for cookie in pickle.load(open('cookies_avito', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(3)
        page = driver.page_source
        page_hh_ru = BeautifulSoup(page, 'html.parser')
        catalog = page_hh_ru.find('div', {'class': 'items-items-kAJAg'})
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

        print('Найдена карточек всего на этом сайте = ', len(project), url_next)


def parse_hh_ru(page_soup_hhru):
    tprint("Parser_HH_Ru")
    time.sleep(3.5)
    page_max = page_soup_hhru.find('div', {'class': 'pager'})
    a_max = page_max.find_all('a', {'class': 'bloko-button'})
    # Поиск и получение максимального количества страниц для цикла
    a_max_int = int(a_max[4].get_text())

    print('Максимальное кол-во страниц = ', a_max_int)
    for h in range(5):
        url_next = url[0] + f'?relocation=living_or_relocation&gender=unknown&search_period=0&page={h}'
        for cookie in pickle.load(open('cookies_hh_ru', 'rb')):
            driver.add_cookie(cookie)
        driver.get(url_next)
        driver.refresh()
        page = driver.page_source
        page_hh_ru = BeautifulSoup(page, 'html.parser')
        time.sleep(2)
        all_crd = page_hh_ru.findAll('div', {'class': 'serp-item'})
        print(url_next)
        for card in all_crd:
            span = card.find_all('span')
            job_age = card.find_all('div', attrs={'data-qa': 'resume-serp__resume-excpirience-sum'})
            project.append({
                'card_job': card.find('a', {'class': 'serp-item__title'}).text,
                'human_age': span[1].text.strip('xa0'),
                'job_status': span[3].text,
                'job_age': span[4].text.strip('xa0'),
                'link': url[0] + card.find('a', {'class': 'serp-item__title'})['href'],
            })


def main():
    parse_hh_ru(get_cookies_hh_ru())
    for projects in project:
        print(projects)
    # parse_avito(get_cookies_avito())
    # for project_ in project:
    #     print(project_)


if __name__ == '__main__':
    main()