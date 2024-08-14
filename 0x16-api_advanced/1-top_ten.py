#!/usr/bin/python3
'''prints the titles of the first 10 hot posts listed for a subreddit'''
import requests


def top_ten(subreddit):
    '''If not a valid subreddit, print None.'''
    url = ('https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit))
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = (data['data']['children'])
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print('None')
