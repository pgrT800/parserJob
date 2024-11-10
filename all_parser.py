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
from selenium.webdriver.chrome.options import Options



tprint('Parsing_xXx')

url = [
    'https://stavropol.hh.ru/search/resume?text={text}&area={area}&age_from={age_from}&age_to={age_to}&employment={employment}&experience={experience}&education_level={education_level}&job_search_status={job_search_status}&relocation={relocation}&schedule=f{schedule}&salary_from={salary_from}&salary_to={salary_to}&gender={gender}&text=&logic=normal&pos=full_text&exp_period=all_time&order_by=relevance&search_period=0&items_on_page=50&no_magic=false',
    'https://trudvsem.ru/cv/search?_regionIds=2600000000000&page=0&salary=0&salary=999999&experience=EXP_STAFF&cvType=LONG', #!
    'https://www.avito.ru/moskva/rezume',
    'https://joblab.ru/search.php?r=res&srregion=50&page=0&submit=1', #!
    'https://stavropol.rabota.ru/v3_searchResumeByParamsResults.html?id=34082135',
    'https://gorodrabot.ru/site/login',
]

project = []


u_ag = UserAgent()
agent = u_ag
optionss = webdriver.ChromeOptions()
service = webdriver.ChromeService(executable_path = 'chromedriver.exe')

optionss.add_argument("--window-size=800,1000")
optionss.add_argument(f'user-agent{agent}')
optionss.add_argument("--disable-blink-features=AutomationControlled")
#prefs = {"profile.default_content_setting_values.notifications": 2}
#optionss.add_argument("prefs", prefs)
optionss.add_argument("--mute-audio")
optionss.add_argument('--ignore-certificate-errors')
optionss.page_load_strategy = 'eager'

driver = webdriver.Chrome(service=service, options=optionss)
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
    # global page_gorod_rabot
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


def get_cookies_rabota_ru():
    try:
        driver.get('https://stavropol.rabota.ru/v3_login.html')
        input_login = driver.find_element(By.NAME, 'login')
        time.sleep(1)
        input_login.send_keys(login_rabota)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(password_rabota)
        time.sleep(1)
        input_password.send_keys(Keys.ENTER)
        pickle.dump(driver.get_cookies(), open('cookies_rabota_ru', 'wb'))
        time.sleep(5)
        driver.get('https://stavropol.rabota.ru/v3_searchResumeByParamsResults.html?id=34082135')
        for cookie in pickle.load(open('cookies_rabota_ru', 'rb')):
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(10)
        page = driver.page_source
        page_rabota_ru = BeautifulSoup(page, 'html.parser')

    except Exception as ex:
        print(ex)
    finally:
        print('Куки rabota_ru успешно загружены =', url[4])
    return page_rabota_ru

def parse_avito(page_soup_avito):
    driver.switch_to.new_window('window')
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
    return project


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
        for project_ in project:
            print(project_)
    return project


def parser_tryd_vsem():
    
    try:
        driver.switch_to.new_window('window')
        driver.get(url[1])
        time.sleep(2)
        div_load = driver.find_element(By.CLASS_NAME, 'main__search-sidebar')
        time.sleep(2)
        button_load = div_load.find_elements(By.TAG_NAME, 'button')
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        visible_button = button_load[0].is_displayed()
        while visible_button == True:
            print('Кнопка есть  = ', visible_button)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print('Прокрутка 1')
            button_visible = div_load.find_elements(By.TAG_NAME, 'button')
            visible_button_dop = button_visible[0].is_displayed()
            if visible_button_dop == False:
                print('Кнопка нет  = ', visible_button_dop)
                print('---------------------------------------------------------------------------------------------')
                break
            else:
                print('Прокрутка 2')
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                button_load[0].click()
            humans = driver.find_elements(By.CLASS_NAME, 'search-results-simple-card')
            time.sleep(2)
            print('Прокрутка 3')
            for project_ in project:
                print(project_)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            with open('progeckt.txt', 'w', encoding="utf-8") as file:
                print('write file')
                file.write(str(project))

            print('Найдено соискателей = ', len(humans))
            time.sleep(2)
        page_driver = driver.page_source
        page_trud_vsem = BeautifulSoup(page_driver, 'html.parser')
        print('\n================================')
        with open("trudvsem.html", "w", encoding="utf-8") as file:
            file.write(page_trud_vsem.prettify())
        time.sleep(8)
        humans_bs = page_trud_vsem.find_all('div', {'class': 'search-results-simple-card mb-1'})
        print(len(humans_bs))
       
        for humans in humans_bs:
            location_all = humans.find_all('div', {'class': 'content_small content_clip'})
            project.append({
                'title': humans.find('strong').text,
                'ZP': humans.find('div', {'class': 'search-results-simple-card__salary'}).text.strip('\n                ').strip('\n            '),
                'last_job': location_all[0].text,
                'location': location_all[1].text,
                'time_publication': humans.find('div', {'class': 'content_pale'}).text,
            })
        

    except Exception as ex:
        print(ex)
        driver.quit()
        driver.close()
    finally:
        print("Куки успешно загружены = ", url[1])
        print('Содержимое проекта', project)
    return(project)


def parer_job_lab(page_job_lab):
    tprint("Parser_Job_Lab")
    time.sleep(6)
    page_max = page_job_lab.find_all('a', {'class': 'pager'})
    int_max_page = int(page_max[6].get_text())
    print('Максимальное кол-во станиц = ', int_max_page)
    for i in range(1, int_max_page):
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
    return project


def parser_gorod_rabot(page_gorod_rabot,driver):
    driver = driver
    driver.switch_to.new_window('window')
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
    
    return project

def parser_rabora_ru(page_rabota_ru):
    try:
        driver.switch_to.new_window('window')
        driver.get(url[4])
        time.sleep(2)
        for cookie in pickle.load(open('cookies_rabota_ru', 'rb')):
            driver.add_cookie(cookie)
        driver.refresh()
        div_load = driver.find_element(By.ID, 'resumeListLoadingIndicator')
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        visible_button = div_load.is_displayed()
        print(visible_button)
        while visible_button == True:
            card_all = driver.find_elements(By.CLASS_NAME, 'b-center__box resum_rez_item')
            print('Найдено всего соискателей = ', len(card_all))
            print('Прокрутка 1')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            div_load_if = driver.find_element(By.ID, 'resumeListLoadingIndicator')
            time.sleep(1)
            visible_button_if = div_load_if.is_displayed()
            # if visible_button_if == False:
            #     print('Кнопка нет  = ', visible_button_if)
            #     print('---------------------------------------------------------------------------------------------')
            #     break
            # else:
            #     print('Прокрутка 2')
            #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #     time.sleep(1)
    except Exception as ex:
        print(ex)
    finally:
        print("Куки успешно загружены = ", url[4])
        driver.quit()


def main():
    #parser_tryd_vsem(project)
    #parser_rabora_ru(get_cookies_rabota_ru())
    # parser_gorod_rabot(get_cookies_gorod_rabot())
    # parer_job_lab(get_cookies_job_lab())
    #parse_hh_ru(get_cookies_hh_ru())
    #parse_avito(get_cookies_avito())
    return

if __name__ == '__main__':
    main()