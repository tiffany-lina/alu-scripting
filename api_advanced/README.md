# Reddit Subscriber Counter

## Overview
Python function `number_of_subscribers(subreddit)` queries the Reddit API and returns the **total number of subscribers** for a subreddit. Returns 0 if the subreddit is invalid.

## Files
- `0-subs.py` – Contains the function.  
- `0-main.py` – Script to test the function.

## Requirements
- Python 3.x
- requests library

Install dependencies:
```bash
pip install requests pycodestyle flake8
# API Advanced — Reddit Top Ten

This project contains functions that interact with the Reddit API.

## Files

- `0-subs.py` — Returns the number of subscribers for a subreddit.
- `1-top_ten.py` — Prints the titles of the first 10 hot posts for a subreddit.
- `0-main.py` — Test file for `0-subs.py`.
- `1-main.py` — Test file for `1-top_ten.py`.

## Requirements

- Custom User-Agent is required to avoid "Too Many Requests".
- Invalid subreddits should return 0 (`0-subs.py`) or print None (`1-top_ten.py`).
- Redirects must **not** be followed.
- All code must be **PEP8 compliant**.
Reddit API advanced project - ALU.
