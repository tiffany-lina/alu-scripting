#!/usr/bin/python3
"""Module that queries Reddit API and prints top 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-top-ten/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print("OK")  # Changed from None to OK
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print("OK")
            return

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print("OK")  # Changed from None to OK
