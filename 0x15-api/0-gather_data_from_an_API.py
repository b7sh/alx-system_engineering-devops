#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url + "users/{}".format(id)).json()
    todo = requests.get(url + "todos", params={"userId": id}).json()

    completed = []
    for element in todo:
        if element.get("completed") is True:
            completed.append(element.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        response.get("name"), len(completed), len(todo)))
    for i in completed:
        print("\t {}".format(i))
