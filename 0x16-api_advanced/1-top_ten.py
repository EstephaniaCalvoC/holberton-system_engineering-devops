#!/usr/bin/python3
"""Define top_ten function"""
import requests


def top_ten(subreddit):
    """
    Query the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x016.project:v1.0.0 (by /u/ecalvoc)"
        }
    params = {"limit": 10}
    top_data = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False).json().get("data")
    if top_data:
        childrens = top_data.get("children")
        [print(children.get("data").get("title")) for children in childrens]
        return
    print("None")
