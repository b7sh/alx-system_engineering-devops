#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(employee_id))
    user = response.json()
    username = user.get("username")
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, username, todo.get(
                "completed"), todo.get("title")])
