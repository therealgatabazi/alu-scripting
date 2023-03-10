#!/usr/bin/python3
"""DOC"""
import requests


def subscribers_count(subreddit_name):
    """DOC"""
    subreddit_url = f"https://www.reddit.com/r/{subreddit_name}/about.json"

    user_agent = {'User-agent': 'Mozilla/5.0'}
    subreddit_response = requests.get(subreddit_url, headers=user_agent)

    if subreddit_response.status_code == 200:
        subreddit_data = subreddit_response.json()['data']
        subscriber_count = subreddit_data['subscribers']
        return subscriber_count
    else:
        return 0
