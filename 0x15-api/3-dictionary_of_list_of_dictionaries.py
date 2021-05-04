#!/usr/bin/python3
"""Export to csv the information about user TODO list progress"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    uri_user = "users"
    uri_todos = "todos"

    users = requests.get(url + uri_user).json()
    dir_user_tasks = {}

    for user in users:
        user_id = user.get("id")
        user_name = user.get("username")
        tasks = requests.get(url + uri_todos,
                             params={"userId": user_id}).json()
        user_tasks = ({user_id: [{"task": task.get("title"),
                                  "completed": task.get("completed"),
                                  "username": user_name} for task in tasks]})
        dir_user_tasks.update(user_tasks)

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(dir_user_tasks, jsonfile)
