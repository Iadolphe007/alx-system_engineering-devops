#!/usr/bin/python3
"""return indromation about employers todo list"""


#!/usr/bin/python3
"""return indromation about employers todo list"""


import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    id_url = "users/{}".format(sys.argv[1])
    url_todo = "todos"
    params = {"userId": sys.argv[1]}
    user = requests.get(url + id_url).json()
    todos = requests.get(url + url_todo, params=params).json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
