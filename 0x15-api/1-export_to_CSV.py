#!/usr/bin/python3
<<<<<<< HEAD
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
                                      
=======
"""
uses a REST API to return inforamtion about an employee given their
employee ID
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos] 
>>>>>>> d3252d752b4991d0402ac65d8849513fdc631b06
