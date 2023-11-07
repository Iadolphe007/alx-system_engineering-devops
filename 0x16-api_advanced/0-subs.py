#!/usr/bin/python3
"""queries Reddit API abd returns numbers of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """queries Reddit API abd returns numbers of subscribers"""

    if subreddit is None or subreddit is not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My-user-Agent'}
    response = requests.get(url, headers=headers).json
    try:
        return response.get('data').get('subscribers')
    except exceptions.RequestException as e:
        return 0
