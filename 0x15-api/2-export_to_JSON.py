#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import json
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
    data_to_dump = {employee_id: []}
    for todo in todos:
        data_to_dump[employee_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })
        with open("{}.json".format(employee_id), "w") as jsonfile:
            json.dump(data_to_dump, jsonfile)
