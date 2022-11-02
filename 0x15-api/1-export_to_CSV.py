#!/usr/bin/python3
""" For a given employee, returns information about the TODO list progress"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    id_ = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_)

    s = requests.Session()

    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_)
    response = s.get(url2)
    name = response.json()['username']

    response = s.get(url)
    body = response.json()

    with open(id_ + '.csv', mode='w') as csv_file:
        employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_ALL)

        for todo in body:
            employee_writer.writerow([id_, name, todo['completed'],
                                      todo['title']])
                                      