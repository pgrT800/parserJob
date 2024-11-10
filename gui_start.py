from tkinter import *
from tkinter import ttk
from all_parser import *


root = Tk()
root.geometry("800x400")

url = ['https://www.avito.ru',
'https://gorodrabot.ru',
'https://stavropol.rabota.ru',
'https://trudvsem.ru',
'https://joblab.ru',
'https://stavropol.hh.ru'
       ]

def get_url_text():
    get_ur = combobox.get()
    if (get_ur == 'https://www.avito.ru'):
        print('avito Выбор') #ban
        parse_avito(get_cookies_avito())
        get_data_for_combox_with_click(get_ur) 

    elif(get_ur == 'https://gorodrabot.ru'):
        print('Gorod-rabot')
        parser_gorod_rabot(get_cookies_rabota_ru())
        get_data_for_combox_with_click(get_ur)

    elif(get_ur == 'https://stavropol.rabota.ru'):
        print('rabota-ru') #not_accept
        #ban
        parser_rabora_ru(get_ur)
        get_data_for_combox_with_click(get_ur)

    elif(get_ur == 'https://trudvsem.ru'):
        print('trudvsem') #accept
        parser_tryd_vsem()
        get_data_for_combox_with_click(get_ur)

    elif(get_ur == 'https://joblab.ru'):
        print('joblab') #accept
        parer_job_lab(get_cookies_job_lab())
        get_data_for_combox_with_click(get_ur)
    elif(get_ur == 'https://stavropol.hh.ru'):
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


combobox = ttk.Combobox(values=url, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", )
btn = Button(root, text='Parsing',command=get_url_text )
btn.pack()



root.mainloop()