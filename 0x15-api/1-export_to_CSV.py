#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}".
                        format(userId), verify=False).json()
    todo = requests.get(url + "todos?userId={}".
                            format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            my_writer.writerow([int(userId), user.get('username'),
                                task.get('completed'), task.get('title')])
