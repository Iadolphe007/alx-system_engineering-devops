#!/usr/bin/python3
"""return indromation about employers todo list"""


import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    url_user = url + "users/{}".format(sys.argv[1])
    url_todo = url + "todos"
    user_id = sys.argv[1]
    params = {"userId": user_id}
    user = requests.get(url=url_user).json()
    todos = requests.get(url=url_todo, params=params).json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
