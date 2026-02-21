#!/usr/bin/python3
"""
This module provides a function that queries the Reddit API and returns the
number of subscribers for a given subreddit.

A custom User-Agent is required to avoid Too Many Requests errors.
Invalid subreddits must return 0 without following redirects.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid
        or if any error occurs.
    """
    if not isinstance(subreddit, str) or subreddit is None:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:api_advanced:v1.0 (by u/student)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
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
