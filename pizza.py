import json
def menu_decorator(func):
    def wrapper(*args, **kwargs):
        menu = func(*args, **kwargs)
        if menu == "Вы ввели некорректную дату рождения":
            print(menu)
        else:
            print("Вот меню: ")
            for elem in menu:
                print(elem)
    return wrapper
def json_load():
    with open('data.json', 'r', encoding='UTF-8') as file:
        try:
            result = json.load(file)
        except json.decoder.JSONDecodeError:
            return []
        else:
            return result

def register(user_info, data):
    for users in data:
        if users['name'] == user_info['name'] and users['surname'] == user_info['surname']:
            return "Пользователь уже существует"
    data.append(user_info)
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    return "Вы успешно зарегистрированы"
@menu_decorator
def print_menu(user_info):
    date = user_info['date of birth'].split('.')
    try:
        year = int(date[2])
    except ValueError:
        return "Вы ввели некорректную дату рождения"
    age = 2024 - year
    if age < 18:
        with open('menu_for_kids.json', 'r', encoding="UTF-8") as menu:
            result = json.load(menu)
            return result
    else:
        with open('menu.json', 'r', encoding="UTF-8") as menu:
            result = json.load(menu)
            return result
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
date_of_birth = input("Введите дату рождения: ")
number = input("Введите номер телефона: ")
user_info = {'name': name, 'surname': surname, 'date of birth': date_of_birth, 'number': number}
data = json_load()
print(register(user_info, data))
print_menu(user_info)
