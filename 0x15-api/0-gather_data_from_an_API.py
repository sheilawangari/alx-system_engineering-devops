#!/usr/bin/python3
<<<<<<< HEAD
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
=======
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed] 
>>>>>>> d3252d752b4991d0402ac65d8849513fdc631b06
