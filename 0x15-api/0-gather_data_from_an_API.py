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
    parms = {"userId": employee_id}
    # .json() converts json string in to a dictionary
    todos_response = requests.get(url + "todos", params=parms)
    todos = todos_response.json()
    completed = []
    for todo in todos:
        if todo["completed"] is True:
            completed.append(todo["title"])
    employee_name = user["name"]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed), len(todo)))
    for index in completed:
        print("\t {}".format(index))
