class PhoneBook:
    def __init__(self, contacts):
        self.contacts = contacts

    def add_contact(self, contact):
        name = contact['name']

        if name in self.contacts:
            print("Name already exists in contacts.")
        else:
            self.contacts[name] = contact

    def get_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            print("Name does not exist.")

    def print_contacts(self):
        print(self.contacts)

    def get_contacts(self):
        return self.contacts