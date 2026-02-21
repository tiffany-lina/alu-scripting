#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts for a given subreddit.

Invalid subreddits should print None. Redirects must not be followed.
A custom User-Agent helps avoid Too Many Requests errors.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Prints:
        The titles of up to 10 hot posts, or None if the subreddit is
        invalid or an error occurs.
    """
    if not isinstance(subreddit, str) or subreddit is None:
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:api_advanced:v1.0 (by u/student)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
    except Exception:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        print(None)
