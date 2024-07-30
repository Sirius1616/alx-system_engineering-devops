#!/usr/bin/python3

"""script that, using this REST API, for a given employee ID, returns 
information about his/her TODO list progress"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    url = base_url + "/" + user_id

    response = requests.get(url)

    employee_name = response.json().get('name')

    to_do_url = url + "/todos"

    response = requests.get(to_do_url)

    tasks = response.json()
    done = 0
    done_task = []

    for task in tasks:
        if tasks.get('completed'):
            done_task.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))



    for task in done_task:
        print("\t {}".format(task.get('title')))




