#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns
the number of subscribers for a given subreddit.

The function uses a custom User-Agent to avoid Too Many Requests errors.
Invalid subreddits return 0 without following redirects.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers. Returns 0 if the subreddit
        is invalid or if any error occurs.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": (
            "linux:api_advanced.subscriber_checker:v1.0 "
            "(by u/yourusername)"
        )
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
        if data is None:
            return 0
        return data.get("subscribers", 0)
    except Exception:
        return 0
