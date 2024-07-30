#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + user_id

    response = requests.get(url)
    EMPLOYEE_NAME = response.json().get('name')

    to_do_url = url + "/todos"
    response = requests.get(to_do_url)
    tasks = response.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = []

    for task in tasks:
        if task.get('completed'):
            TOTAL_NUMBER_OF_TASKS.append(task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, len(TOTAL_NUMBER_OF_TASKS)))


    for task in TOTAL_NUMBER_OF_TASKS:
        print("\t {}".format(task.get('title')))




