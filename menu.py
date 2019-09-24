from PhoneBook import PhoneBook
from json_helper import load_book, save_book
from test import test_phone_book


def main():
    phone_book = PhoneBook(load_book())

    while True:
        print('--- Phone Book ----')
        print('1.Add a new contact.\n'
              '2.Search a contact.\n'
              '3.Display Contacts.\n'
              '4.Exit\n')

        option = input("Enter option: ")
        if option == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            contact = {'name': name, 'phone': phone}
            phone_book.add_contact(contact)
        elif option == '2':
            name = input("Enter name: ")
            print(phone_book.get_contact(name))
        elif option == '3':
            phone_book.print_contacts()
        elif option == '4':
            save_book(phone_book.get_contacts())
            print('Exiting program...')
            break


main()
