
path = 'phonebook.txt'

def create_open_file():
    data = open(path, 'a', encoding = 'UTF-B')
    data.close

#def close_file():
#    data = 

def adding_into_file():
    data = open(path, 'a', encoding='UTF-8')
    name = input("Введите имя: ").capitalize()
    middle_name = input("Введите отчество: ").capitalize()
    surname = input("Введите фамилию: ").capitalize()
    phone = input("Введите номер телефона: ")
    data.write(f"{name} {middle_name} {surname} {phone}")
    data.close

def reading_file():
    data = open(path, 'r', encoding='UTF-8')
    print(data.read())
    data.close()

def finding_contact_file():
    data = open(path, 'r', encoding='UTF-8')
    finding_contact = input("Введите искомые параметры: ")
    in_finding_text = data.readlines()
    dict_contacts = {}
    for i, j in enumerate(in_finding_text, 1):
        j = j.strip()
        dict_contacts = {'name': in_finding_text[0], 'middle_name': in_finding_text[1], 'surname': in_finding_text[2], 'phone': in_finding_text[3] }
    for i in in_finding_text:
        if i == finding_contact:
            print(dict_contacts['name'])















