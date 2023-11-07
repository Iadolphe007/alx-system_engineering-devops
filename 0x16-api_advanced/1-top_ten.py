#!/usr/bin/python3
"""reddit querries"""


def top_ten(subreddit):
    """prints the titles if the first hot 10 posts"""
    import requests

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False).json
    try:
        data = response.get('data').get('children')
        for i in data:
            print(i.get('data').get('title'))
    except Exception:
        print('None')
