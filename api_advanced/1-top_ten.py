#!/usr/bin/python3
"""This script prints the top ten posts from a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the top ten posts from a given subreddit."""
    # Construct the URL for the given subreddit
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set the user-agent header
    headers = {'User-agent': 'Mozilla/5.0'}

    # Make the API request
    response = requests.get(reddit_url, headers=headers)

    # If the request is successful, print the titles of the top ten posts
    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])
    # If the request fails, print None
    else:
        print(None)
