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
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    # .json() converts json string in to a dictionary
    todo = requests.get(url + "todos", params={"userId": id}).json()
    filename = "{}.csv".format(id)
    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for do in todo:
            writer.writerow([id, username, do.get(
                "completed"), do.get("title")])
