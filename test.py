def test_phone_book():
    t_contacts = {
        'Jon Smith': {'name': 'John Smith', 'phone number': '787-456-9078', 'email': 'johnsmith@john.com'},
        'Arthur Gold': {'name': 'Arthur Gold', 'phone number': '787-556-9058', 'email': 'arthurgold@john.com'}
    }

    contact = {'name': 'Tyrone Rahl', 'phone number': '787-556-9078', 'email': 'tyrone@john.com'}
    b1 = PhoneBook(t_contacts)
    b1.printContacts()
    b1.add_contact(contact)
    b1.printContacts()
    b1.add_contact(contact)