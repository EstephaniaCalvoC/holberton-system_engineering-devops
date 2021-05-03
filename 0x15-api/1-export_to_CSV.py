#!/usr/bin/python3
"""Export to csv the information about user TODO list progress"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    uri_user_id = "users/{}".format(user_id)
    uri_todos = "todos"

    user_name = requests.get(url + uri_user_id).json().get("username")
    tasks = requests.get(url + uri_todos, params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id,
             user_name,
             task.get("completed"),
             task.get("title")]
         ) for task in tasks]
