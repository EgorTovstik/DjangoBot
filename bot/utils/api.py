import requests
import json


DATABASE_URL = 'http://127.0.0.1:8000/api/v1'


# Функция создания нового пользователя в таблице "Пользователи"
def create_user(tg_id, name, phone_num, consent_mail_list):
    url = f"{DATABASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["tg_ID"] == str(tg_id):
            user_exist = True
            break
    if user_exist == False:
        requests.post(url=url, data={
            "tg_ID": tg_id,
            "name": name,
            "phone_num": phone_num,
            "consent_mail_list": consent_mail_list
        })
        return "Пользователь успешно загружен"
    else:
        return "Вы уже зарегистрированы!"


# Функция создания результатов опроса в таблице "Опросы"
def create_survey(tg_id, quest1, quest2, quest3, quest4):
    url = f"{DATABASE_URL}/surveys"
    if quest1 and quest2 and quest3 and quest4:
        post = requests.post(url=url, data={
            "tg_ID": tg_id,
            "quest1": quest1,
            "quest2": quest2,
            "quest3": quest3,
            "quest4": quest4
        })
        return "Результаты опроса сохранены"
    else:
        return "Результаты опроса не сохранены"


# Функция получения текста из таблицы "Рассылка"
def get_mailing_text(id):
    url_mailing = f"{DATABASE_URL}/mail-list"
    response_mailing = requests.get(url=url_mailing)
    data = response_mailing.json()
    return data

