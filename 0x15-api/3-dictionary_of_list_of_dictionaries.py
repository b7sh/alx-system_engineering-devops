#!/usr/bin/python3
""" to-do list information of all employees to JSON format. """
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users")
    users = response.json()
    data = {}
    for user in users:
        employee_id = user.get("id")
        params = {"userId": employee_id}
        user_data = []
        todo_response = requests.get(url + "todos", params=params)
        todos = todo_response.json()
        for todo in todos:
            task_data = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
            }
            user_data.append(task_data)
            data[employee_id] = user_data
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
