close_phone_book = False

path = "PhoneBook.txt"

def scan(path):
    data = open(path, 'r')
    for i in data:
        print(i)

def change(path):
    file = open(path, 'r')
    data = input("Add data for finding: ")
    new_data = input("Add new data: ")
    lines = []
    for line in file:
        if data in line.split(" "):
            line = line.replace(data, new_data)
        lines.append(line)
    file.close()
    file = open(path, 'w')
    file.write("".join(lines))
    file.close()


def remove(path):
    file = open(path, 'r')
    data = input("Add data for removing: ")
    lines = []
    for line in file:
        if data not in line.split(" "):
            lines.append(line)
    file.close()
    file = open(path, 'w')
    file.write("".join(lines))
    file.close()


def find(path):
    file = open(path, 'r')
    data = input("Add data for finding: ")
    for line in file:
        if data in line.split(" "):
            print(line)
    file.close()


def add(path):
    data = open(path, 'a')
    name = input("Add first name: ")
    middle_name = input("Add middle name: ")
    surname = input("Add surname: ")
    phone_number = int(input("Add phone number: "))
    data.writelines(f"{name} {middle_name} {surname} {phone_number} \n")
    data.close()

def exit(path):
    global close_phone_book
    close_phone_book = True

commands_dict = {1: scan, 2: change, 3: remove, 4: find, 5: add, 6: exit}

while not close_phone_book:
    print("Choose action: ")
    print("1 - Scan contacts")
    print("2 - Change contacts")
    print("3 - Remove contacts")
    print("4 - Find contacts")
    print("5 - Add contacts")
    print("6: Exit")
    command = commands_dict[int(input("Add action: "))]
    if command:
        command(path)