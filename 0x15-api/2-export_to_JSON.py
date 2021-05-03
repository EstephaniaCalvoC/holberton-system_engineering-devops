#!/usr/bin/python3
"""Export to csv the information about user TODO list progress"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    uri_user_id = "users/{}".format(user_id)
    uri_todos = "todos"

    user_name = requests.get(url + uri_user_id).json().get("username")
    tasks = requests.get(url + uri_todos, params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w", newline="") as jsonfile:
        json.dump({user_id: [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": user_name} for task in tasks]},
                  jsonfile)
