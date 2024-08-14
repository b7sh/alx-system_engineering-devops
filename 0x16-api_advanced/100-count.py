#!/usr/bin/python3
'''parses the title of all hot articles,
and prints a sorted count of given keywords'''
import requests


def count_words(subreddit, word_list, after_value=None, word_counts=None):
    '''If no posts match or the subreddit is invalid, print nothing.'''
    if word_counts is None:
        word_counts = {}
    url = ('https://www.reddit.com/r/{}/hot.json'.format(subreddit))
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            title_words = title.split()
            for element in word_list:
                element = element.lower()
                if element in title_words:
                    if element in word_counts:
                        word_counts[element] += 1
                    else:
                        word_counts[element] = 1

        after_value = data['data']['after']
        if after_value:
            count_words(subreddit, word_list, after_value, word_counts)
        else:
            sorted_counts = sorted(
                word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
