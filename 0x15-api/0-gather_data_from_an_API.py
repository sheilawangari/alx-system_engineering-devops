#!/usr/bin/python3
""" For a given employee, returns information about the TODO list progress"""
import requests
from sys import argv


if __name__ == '__main__':
    id_ = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_)

    s = requests.Session()

    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_)
    response = s.get(url2)
    name = response.json()['name']

    response = s.get(url)
    body = response.json()
    tasks_done = []
    for b in body:
        if b['completed']:
            tasks_done.append('\t ' + b['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(tasks_done), len(body)))
    print(*tasks_done, sep='\n')
