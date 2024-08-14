#!/usr/bin/python3
'''Returns the titles of the all hot articles listed for a subreddit'''
import requests


def recurse(subreddit, hot_list=[], after_value=None):
    '''If not a valid subreddit, print None.'''
    url = ('https://www.reddit.com/r/{}/hot.json'.format(subreddit))
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 400:
        return None
    else:
        data = response.json()
        posts = (data['data']['children'])
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        after_value = data['data']['after']
        if after_value:
            return recurse(subreddit, hot_list, after_value)
        else:
            return hot_list
