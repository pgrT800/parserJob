import requests
from bs4 import BeautifulSoup
import time
import csv
from art import tprint
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pickle
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://stavropol.hh.ru/search/resume?relocation=living_or_relocation&gender=unknown&search_period=0'
url_filter = 'https://stavropol.hh.ru/search/resume?relocation=living_or_relocation&gender=unknown&text=&logic=normal&pos=full_text&exp_period=all_time&order_by=relevance&search_period=0&items_on_page=50&no_magic=false'


u_ag = UserAgent()
agent = u_ag.random
options = webdriver.EdgeOptions()
# options.add_argument(f'user-agent{agent}')
# options.add_argument("--headless")
driver = webdriver.ChromiumEdge(options=options)
driver.maximize_window()
driver.execute_script("window.stop();", 1)


def parse_filters():
    tprint('HH_RU_FILTERS')
#     Значения переезда living_or_relocation \ living \living_but_relocation \ relocation
    relocation = input('Введите одну из категрий  переезда = living_or_relocation \ living \living_but_relocation \ relocation = ')
    job_search_status = input('Введите один из статус поиска \ unknown \ not_looking_for_job \ looking_for_offers \ active_search \ has_job_offer \ accepted_job_offer = ')
    age_from = input('Введите возраст от = ')
    age_to = input('Введите возраст до = ')
    employment = input('Введите один из типов занятости \ full \ part \ progect \ probation \ volunteer = ')
    schedule = input('Введите один из типов расписания \ fullDay \ shift \ flexible \ remote \ flyInFlyOut  = ')
    experience = input('Ведите опыт работы \ moreThan6 \ between3And6 \ noExperience \ between1And3 \  = ')
    gender = input('Введите один из гenders \ unknown \ male \ female \ = ')
    salary_from = input('Введите доход от = ')
    salary_to = input('Введите доход до = ')
    education_level = input('Введите один из уровней образования \ secondary \ specisl_secondary \ unfinished_higher \ bachelor \ master \ higher \ candidate \ doctor = ')
    url_filters = f'https://stavropol.hh.ru/search/resume?&age_from={age_from}&age_to={age_to}&employment={employment}&experience={experience}&education_level={education_level}&job_search_status={job_search_status}&relocation={relocation}&schedule=f{schedule}&salary_from={salary_from}&salary_to={salary_to}&gender={gender}&text=&logic=normal&pos=full_text&exp_period=all_time&order_by=relevance&search_period=0&items_on_page=50&no_magic=false'
    driver.get(url_filters)
    time.sleep(30)


def main():
    parse_filters()


if __name__ == '__main__':
    main()