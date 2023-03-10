#!/usr/bin/python3
"""This module contains functions for working with the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieves the titles of hot articles from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param)

    if response.status_code != 200:
        return None
    else:
        json_res = response.json()
        after = json_res.get('data').get('after')
        has_next = json_res.get('data').get('after') is not None
        hot_articles = json_res.get('data').get('children')
        hot_list += [article['data']['title'] for article in hot_articles]

        return recurse(subreddit, hot_list, after=after) if has_next else hot_list
