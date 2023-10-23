#!/usr/bin/python3
"""
export to json
"""

import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}".
                        format(userId), verify=False).json()
    todo = requests.get(url + "todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.json".format(userId), "w") as json_file:
        json.dump({userId: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todo]}, json_file)
