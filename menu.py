phone_book = {'Antonio Roman': {'name': 'Antonio Roman', 'phone': '783-544-5393'},
              'John Lewi': {'name': 'John Lewi', 'phone': '434-543-5124'}}


def add_contact():
    print('Add contact here')


def search_contact(name) :
    return True


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
        print('Exiting program...')
        break
