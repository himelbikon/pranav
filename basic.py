import json
import os


def write_json():
    json.dump(
        {'database': database},
        open('DB.json', 'w')
    )


def add_data():
    data_input = input('Enter a data to input: ')
    database.append(data_input)
    write_json()


def remove_data():
    if not database:
        print('There is no data the database.')
        return

    data_input = input('Enter a data to remove: ')

    if data_input in database:
        database.remove(data_input)
        write_json()
    else:
        print(f'"{data_input}" does not exist in the database!')


database = []

if os.path.exists('DB.json'):
    json_content = json.load(open('DB.json', 'r'))
    database = json_content['database']


if __name__ == '__main__':
    while True:
        print('----- Printing our Rookie Database -----')

        for index, name in enumerate(database, 1):
            print(f'{index}) {name}')

        user_input = input('Type keyword here: ')

        if user_input == 'add':
            add_data()
        elif user_input == 'remove':
            remove_data()
        else:
            print('Please input a valid keyword!')
