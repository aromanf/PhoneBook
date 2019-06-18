import json


def save_book() :
    with open('data_file.json', 'w') as write_file:
        json.dump(phone_book, write_file)


def load_book() :
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        return data


def add_contact():
    print('Add contact here')


def search_contact(name):
    return True


phone_book = load_book()

while True:
    print('--- Phone Book ----')
    print('1.Add a new contact.\n'
          '2.Search a contact.\n'
          '3.Display Contacts.\n'
          '4.Exit\n')

    option = input("Enter option: ")
    if option == '1':
        add_contact()
    elif option == '2':
        name = input("Enter name: ")
        search_contact(name)
    elif option == '3':
        print(phone_book)
    elif option == '4':
        save_book()
        print('Exiting program...')
        break
