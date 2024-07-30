#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + user_id

    response = requests.get(url)
    employeeName = response.json().get('name')

    to_do_url = url + "/todos"
    response = requests.get(to_do_url)
    tasks = response.json()
    done = 0
    done_task = []

    for task in tasks:
        if task.get('completed'):
            done_task.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))


    for task in done_task:
        print("\t {}".format(task.get('title')))




