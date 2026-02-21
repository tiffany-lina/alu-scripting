#!/usr/bin/python3
"""
Function that queries the Reddit API and returns number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit.
    If subreddit is invalid, returns 0.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "linux:subscriber.counter:v1.0 (by u/yourusername)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
    except Exception:
        return 0

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        return data.get("subscribers", 0)
    except Exception:
        return 0
