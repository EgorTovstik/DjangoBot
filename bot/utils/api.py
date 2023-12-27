import requests
import json


DATABASE_URL = 'http://127.0.0.1:8000/api/v1'


def create_user(tg_id, name, phone_num):
    url = f"{DATABASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["tg_ID"] == str(tg_id):
            user_exist = True
            break
    if user_exist == False:
        requests.post(url=url, data={"tg_ID": tg_id, "name": name, "phone_num": phone_num})
        return "Пользователь успешно загружен"
    else:
        return "Вы уже зарегистрированы!"


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

