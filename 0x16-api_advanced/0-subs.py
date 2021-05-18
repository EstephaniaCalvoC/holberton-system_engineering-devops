#!/usr/bin/python3
"""Define number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    - If an invalid subreddit is given, the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x016.project:v1.0.0 (by /u/ecalvoc)"
        }
    subreddit_data = requests.get(url,
                                  headers=headers,
                                  allow_redirects=False).json().get("data")
    if subreddit_data:
        return subreddit_data.get("subscribers")
    return 0
