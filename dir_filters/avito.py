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


project = []

u_ag = UserAgent()
agent = u_ag.random
options = webdriver.EdgeOptions()
# options.add_argument(f'user-agent{agent}')
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
# Верхния строчка опций отвечает за фоновую работу браузера
driver = webdriver.Edge(options=options)

# options.set_preference("dom.webdriver.enabled", False)
print(agent)


def get_cookies_avito():
    # Подгрузка куки авито и возвращение обьекта bs4
    try:
        driver.get('https://www.avito.ru/amurskaya_oblast_svobodnyy/rezume/bez_opyta_studenty-ASgBAgICAUSUC_6eAQ?p=1')
        time.sleep(4)
        page = driver.page_source
        page_soup_avito = BeautifulSoup(page, 'html.parser')
        for cookie in pickle.load(open('cookies_avito_ru', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(2)
        driver.refresh()
        time.sleep(10)
    except Exception as ex:
        print(ex)

    finally:
        print("Куки авито успешно загружены = ", 'https://www.avito.ru/amurskaya_oblast_svobodnyy/rezume/bez_opyta_studenty-ASgBAgICAUSUC_6eAQ?p=1')

    return page_soup_avito


def parse_avito(page_soup_avito):
    tprint("Parser_Avito")
    time.sleep(6)
    page_max = page_soup_avito.find('div', {'class': 'js-pages pagination-pagination-_FSNE'}).find_all('span', {'class': 'styles-module-text-InivV'})
    int_max_page = int(page_max[6].get_text())
    print('Максимальное кол-во станиц = ', int_max_page)
    i = 2
    for i in range(1, int_max_page, + 1):
        url_next = 'https://www.avito.ru/amurskaya_oblast_svobodnyy/rezume/bez_opyta_studenty-ASgBAgICAUSUC_6eAQ?p=1' + f'?p={i}'
        driver.get(url_next)
        for cookie in pickle.load(open('cookies_avito_ru', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(3)
        page = driver.page_source
        page_hh_ru = BeautifulSoup(page, 'html.parser')
        catalog = page_hh_ru.find('div', {'class': 'items-items-kAJAg'})
        card_all = catalog.find_all('div', {'class': 'iva-item-body-KLUuy'})
        for card in card_all:
            card_p = card.find('p')
            i = 0
            print('Длинна карточки', len(card_p))
            # p = card_text.find('p')
            # if p == None:
            #     p = ''
            # else:
            #     p = p
            project.append({
                'name': card.find('h3', {'class': 'styles-module-root-TWVKW styles-module-root-_KFFt styles-module-size_l-_oGDF styles-module-size_l-hruVE styles-module-ellipsis-LKWy3 styles-module-weight_bold-Kpd5F stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-header-l-qvNIS'}).text,
                'ZP': card.find('span', {'class': ''}).text,
                'gender/time_jobs': card.find('span', {'class': 'styles-module-noAccent-nZxz7 styles-module-size_s-awPvv'}).get_text(),
                # 'description': card,
                # 'description': p[i].text,
                # 'time_publication': p[y].text,
            })

        print('Найдена карточек всего на этом сайте = ', len(project), url_next)
    return project


def main():
    parse_avito(get_cookies_avito())
    for project_ in project:
        print(project_)

if __name__ == '__main__':
    main()