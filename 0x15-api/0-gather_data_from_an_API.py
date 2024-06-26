#!/usr/bin/python3
"""using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(employee_id))
    user = response.json()
    params = {"userId": employee_id}
    params_2 = {"userId": employee_id, "completed": "true"}
    todos_response = requests.get(url + "todos", params=params)
    todos = todos_response.json()
    completed = requests.get(url + "todos", params=params_2).json()
    employee_name = user["name"]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed), len(todos)))
    for index in completed:
        print("\t {}".format(index['title']))
