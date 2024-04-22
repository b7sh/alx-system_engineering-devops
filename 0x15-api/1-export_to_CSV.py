#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
import sys
import csv


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    # .json() converts json string in to a dictionary
    todo = requests.get(url + "todos", params={"userId": id}).json()
    filename = "{}.csv".format(id)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for do in todo:
            writer.writerow([id, user.get("username"), do["completed"], do["title"]])
