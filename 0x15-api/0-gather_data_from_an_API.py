#!/usr/bin/python3
"""Return information about his/her TODO list progress"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    uri_user_id = "users/{}".format(user_id)
    uri_todos = "todos"

    user = requests.get(url + uri_user_id).json()
    tasks = requests.get(url + uri_todos, params={"userId": user_id}).json()

    tasks_completed = [task for task in tasks if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(tasks_completed),
                                                          len(tasks)))

    [print("\t {}".format(task.get("title"))) for task in tasks_completed]
