#!/usr/bin/python3
<<<<<<< HEAD
""" For a given employee, returns information about the TODO list progress"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    id_ = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_)

    s = requests.Session()

    url2 = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_)
    response = s.get(url2)
    name = response.json()
    name = name.get('username')

    response = s.get(url)
    body = response.json()

    data = {id_: []}
    for task in body:
        data[id_].append({"task": "{}".format(task.get('title')),
                          "completed": task.get('completed'),
                          "username": "{}".format(name)})

    with open(id_ + '.json', 'w') as outfile:
        json.dump(data, outfile)
        
=======
"""
uses a REST API to return inforamtion about an employee given their
employee ID
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
>>>>>>> d3252d752b4991d0402ac65d8849513fdc631b06
