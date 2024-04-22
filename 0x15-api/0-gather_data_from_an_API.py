#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    # .json() converts json string in to a dictionary
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()
    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee{}is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    for index in completed:
        print("\t{}".format(index))
