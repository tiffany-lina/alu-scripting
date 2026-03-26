#!/usr/bin/python3
"""
1-top_ten.py
Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "ALU-project:top_ten:v1.0 (by /u/ubuntu)"}

    try:
        # Do not follow redirects (invalid subreddit will redirect)
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)

        # Invalid subreddit (redirect or not 200)
        if response.status_code != 200:
            print(None)
            return

        # Extract posts safely
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post["data"].get("title"))

    except Exception:
        print(None)
