#!/usr/bin/python3
"""
0-main.py
Tests the number_of_subscribers function.
"""

import sys
number_of_subscribers = __import__('0-subs').number_of_subscribers

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
