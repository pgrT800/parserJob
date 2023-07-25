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
from test_dir.test import print_def

url = [
    'https://stavropol.hh.ru/search/resume',
    'https://trudvsem.ru/cv/search?_regionIds=2600000000000&page=0&salary=0&salary=999999&experience=EXP_STAFF&cvType=LONG',
    'https://www.avito.ru/moskva/rezume',
    'https://joblab.ru/search.php?r=res&srregion=50&page=0&submit=1',
    'https://www.rabota.ru/v3_login.html',
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


def get_cookies_job_lab():
    try:
        driver.get(url[3])
        time.sleep(3)
        for cookie in pickle.load(open('cookies_job_lab', 'rb')):
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(5)
        page = driver.page_source
        page_job_lab = BeautifulSoup(page, 'html.parser')
    except Exception as ex:
        print(ex)
    finally:
        print("Куки авито успешно загружены = ", url[3])

    return page_job_lab


def get_cookies_gorod_rabot():
    try:
        driver.get(url[5])
        # time.sleep(3)
        # login_email = driver.find_element(By.NAME, 'email')
        # login_email.send_keys(login_gorod_rabot)
        # time.sleep(1)
        # password = driver.find_element(By.NAME, 'password')
        # password.send_keys(password_gorod_rabot)
        # time.sleep(1)
        # password.send_keys(Keys.ENTER)
        # pickle.dump(driver.get_cookies(), open('cookies_gorod_rabot', 'wb'))
        # time.sleep(5)
        for cookie in pickle.load(open('cookies_gorod_rabot', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(2)
        driver.refresh()
        time.sleep(3)
        driver.get('https://moskva.gorodrabot.ru/resumes?p=1000')
        time.sleep(4)
        page = driver.page_source
        page_gorod_rabot = BeautifulSoup(page, 'html.parser')
    except Exception as ex:
        print(ex)
    finally:
        print("Куки gorod_rabot успешно загружены = ", url[4])

    return page_gorod_rabot


def parse_avito(page_soup_avito):
    tprint("Parser_Avito")
    time.sleep(6)
    page_max = page_soup_avito.find('div', {'class': 'js-pages pagination-pagination-_FSNE'}).find_all('span', {'class': 'styles-module-text-InivV'})
    int_max_page = int(page_max[6].get_text())
    print('Максимальное кол-во станиц = ', int_max_page)
    i = 2
    for i in range(1, int_max_page, + 1):
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
    for h in range(a_max_int):
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


def parer_job_lab(page_job_lab):
    tprint("Parser_Job_Lab")
    time.sleep(6)
    page_max = page_job_lab.find_all('a', {'class': 'pager'})
    int_max_page = int(page_max[6].get_text())
    print('Максимальное кол-во станиц = ', int_max_page)
    for i in range(1, 4):
        url_next = f'https://joblab.ru/search.php?r=res&srregion=50&page={i}&submit=1'
        driver.get(url_next)
        for cookie in pickle.load(open('cookies_job_lab', 'rb')):
            driver.add_cookie(cookie)
        page_job_lab = BeautifulSoup(driver.page_source, 'html.parser')
        name_all = page_job_lab.find_all('p', {'class': 'prof'})
        table = page_job_lab.find('tbody')
        td = table.find_all('td', {'class': ''})[9:]

        print(url_next)
        print(len(name_all))
        i = -1
        for name in name_all:
            p = page_job_lab.find_all('p', attrs={'style': 'font-size:16px; padding:6px 0 6px 0;'})
            y = page_job_lab.find_all('p', attrs={'style': 'font-size:15px; padding:6px 0 6px 0; color:#555;'})
            zp = page_job_lab.find_all('td', {'class': 'hhide680'})
            print(len(p))
            i = i + 1
            print('i = ', i)
            project.append({
                'name_job': name.find('a', attrs={'target': '_blank'}).text,
                'name/age': p[i].text,
                'job_age': y[i].text,
                'zp': zp[i].find('p').text,
            })
        i = 0


def parser_gorod_rabot(page_gorod_rabot):
    tprint('Parser_Gorod_rabot')
    # Поиск максимального кол во страниц
    page_max_ul = page_gorod_rabot.find('ul', {'class': 'result-list__pager pager'})
    a_page = page_gorod_rabot.find_all('a', {'class': 'pager-item'})
    a_page = a_page[4]['href'].split('https://moskva.gorodrabot.ru/resumes?p=')
    int_max_page = int(a_page[1])
    print('Максимальное кол - во страниц = ', int_max_page)
    for i in range(1, int_max_page + 1):
        url_next = f'https://moskva.gorodrabot.ru/resumes?p={i}'
        driver.get(url_next)
        for cookie in pickle.load(open('cookies_gorod_rabot', 'rb')):
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(1)
        page_gorod = BeautifulSoup(driver.page_source, 'html.parser')
        lists_crd = page_gorod.find('div', {'class': 'result-list'})
        all_crd = lists_crd.find_all('div', {'class': 'result-list__snippet snippet'})
        for card in all_crd:
            i = 2
            location = card.find_all('span', {'class': 'snippet__meta-value'})
            project.append({
                'name_job': card.find('a', {'class': 'snippet__title-link link'}).text,
                'ZP': card.find('span', {'class': 'snippet__salary'}).text.strip('xa').strip('\n').strip('                    ').strip('\n'),
                'age': card.find('span', {'class': 'snippet__meta-value'}).text.strip('\n                    ').strip('\n                        \n'),
                'location': location[1].text.strip('').strip('\n                        ').strip('                    '),
                'discriptons': card.find('div', {'class': 'snippet__desc'}).text.strip('\n                ').strip('  ...             '),
                'time_publication': card.find('div', {'class': 'snippet__source'}).text.strip('\n                    ').strip('                '),
                'link': card.find('a', {'class':'snippet__title-link link'})['href'],
            })
        print(url_next)
        print('Найдено всего соискателей = ', len(project))


def main():
    print_def()
    # parser_gorod_rabot(get_cookies_gorod_rabot())
    # for project_ in project:
    #     print(project_)
    # parer_job_lab(get_cookies_job_lab())
    # for projects in project:
    #     print(projects)
    # parse_hh_ru(get_cookies_hh_ru())
    # for projects in project:
    #     print(projects)
    # parse_avito(get_cookies_avito())
    # for project_ in project:
    #     print(project_)


if __name__ == '__main__':
    main()