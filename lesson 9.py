
main_menu = '''\nГлавное меню:
    1. Отрыть файл
    2. Записать файл
    3. Показать контакт
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load= телефонная книга успешно открыта

import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_message(message: str):
    print(\n + = )


def print_contact(pb: list[dict[str, str]], error: str):
    if pb:
        for contact in enumerate(pb, 1):
            print('f{i}. {contact.get("name'):<20
        print()
    else:
        print_message(error)

def get_pb() -> list[dict]


import view

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_gb()
                view.print_message(text.load_successful)
            case 2:
                pass
            case 3:
                print(model.phone_book)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break





import controller

if __



phone_book = []
path = 'phone.txt'

def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})



def input_contact(message: str) -> dict:
    contact = {}
    print(message)
    for key. value in text.input_contact.items()
    name = input()
    phone = input()
    book = input()

