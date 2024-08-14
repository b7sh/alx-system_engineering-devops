#!/usr/bin/python3
"""Returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
	"""Return the total number of subscribers."""
	url = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
	response = requests.get(url, allow_redirects=False)
	if response.status_code == 200:
		data = response.josn()
		return data['data']["subscribers"]
	else:
		return 0
