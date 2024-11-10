from tkinter import *
from tkinter import ttk
from all_parser import *

root = Tk()
root.geometry("800x400")

url_list = [
('https://www.avito.ru/moskva/rezume'),
('https://gorodrabot.ru/site/login'),
('https://stavropol.rabota.ru/v3_searchResumeByParamsResults.html?id=34082135'),
('https://trudvsem.ru/cv/search?_regionIds=2600000000000&page=0&salary=0&salary=999999&experience=EXP_STAFF&cvType=LONG'),
('https://joblab.ru/search.php?r=res&srregion=50&page=0&submit=1'),
('https://stavropol.hh.ru/search/resume?text=&area=&age_from=&age_to=&employment=&experience=&education_level=&job_search_status=&relocation='),
]

def get_url_text():
    get_ur = combobox.get()
    if (get_ur == 'https://www.avito.ru/moskva/rezume'):
        print('avito Выбор') #ban
        parse_avito(get_cookies_avito())
        get_data_for_combox_with_click(get_ur) 

    elif(get_ur == 'https://gorodrabot.ru/site/login'):
        print('Gorod-rabot')
        parser_gorod_rabot(get_cookies_rabota_ru())
        get_data_for_combox_with_click(get_ur)

    elif(get_ur == 'https://stavropol.rabota.ru/v3_searchResumeByParamsResults.html?id=34082135'):
        print('rabota-ru') #not_accept
        #ban
        parser_rabora_ru(get_ur)
        get_data_for_combox_with_click(get_ur)

    elif(get_ur == 'https://trudvsem.ru/cv/search?_regionIds=2600000000000&page=0&salary=0&salary=999999&experience=EXP_STAFF&cvType=LONG'):
        print('trudvsem') #accept
        parser_tryd_vsem()
        get_data_for_combox_with_click(get_ur)

    elif(get_ur == 'https://joblab.ru/search.php?r=res&srregion=50&page=0&submit=1'):
        print('joblab') #accept
        parer_job_lab(get_cookies_job_lab())
        get_data_for_combox_with_click(get_ur)
    elif(get_ur == 'https://stavropol.hh.ru/search/resume?text=&area=&age_from=&age_to=&employment=&experience=&education_level=&job_search_status=&relocation='):
        print('hhru')
        parse_hh_ru(get_cookies_hh_ru())
        get_data_for_combox_with_click(get_ur)
    else:
        print("Unknown")
    return get_ur

def get_data_for_combox_with_click(get_ur):
    url = get_ur
    print(url,'проверка')
    return url


combobox = ttk.Combobox(values=url_list, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", )
btn = Button(root, text='Parsing',command=get_url_text )
btn.pack()


root.mainloop()