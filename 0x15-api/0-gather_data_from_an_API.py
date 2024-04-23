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
    response = requests.get(url + "users/{}".format(employee_id))
    user = response.json()
    # .json() converts json string in to a dictionary
    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    todos = todos_response.json()
    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    employee_name = user.get("name")
    employee_name_fixed = employee_name[:18].ljust(18)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name_fixed, len(completed), len(todo)))
    for index in completed:
        print("\t {}".format(index))
