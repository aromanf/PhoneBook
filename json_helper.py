import json


def save_book(data) :
    with open('data_file.json', 'w') as write_file:
        json.dump(data, write_file)


def load_book() :
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        return data