#!/usr/bin/python3
"""recursive Api"""


def recurse(subreddit, hot_list=[]):
    """return 10 hot post using recursive api"""

    import requests
    after = None

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My-user-agent'}
    params = {'after': 'after', 'count': 'count'}
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('after')
        if data is not None:
            after = data
            recurse(subreddit, hot_list)
        titles = response.json().get('data').get('children')
        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return (None)
