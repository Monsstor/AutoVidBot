import praw
import os
import sys
import subprocess
import math
import settings
from pathlib import Path
import json
import time


# Reddit API credentials
CLIENT_ID = settings.REDDIT_CLIENT_ID
CLIENT_SECRET = settings.REDDIT_CLIENT_SECRET
USERNAME = settings.REDDIT_CLIENT_USERNAME
PASSWORD = settings.REDDIT_CLIENT_PASSWORD
USER_AGENT = "Reddit Video Maker (by /u/321rikraw)"  # Change this to your Reddit username

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT,
)

def fetch_content(subreddit_list):
    start_time = time.time()
    reddit_content = []
    while len(reddit_content) < 10:
        for subreddit_name in subreddit_list:
            subreddit = reddit.subreddit(subreddit_name)
            count = 0
            while count==0:
                top_posts = subreddit.top(limit=5)
                for post in top_posts:
                    if post.title not in [content["title"] for content in reddit_content]:
                        count = 1
                        top_comments = []
                        for comment in post.comments:
                            if comment.body == "[deleted]" or "bot" in comment.body:
                                continue
                            else:
                                top_comments.append(comment.body)
                            if len(top_comments) == 3:
                                break
                            
                        reddit_content.append({
                            "title": post.title,
                            "description": post.selftext,  # Include post description
                            "url": post.url,
                            "score": post.score,
                            "com1": top_comments[0],
                            "com2": top_comments[1],
                            "com3": top_comments[2]
                        }) 
    with open("reddit_content.json", "w") as json_file:
        json.dump(reddit_content, json_file, indent=4)
    end_time = time.time()
    return end_time - start_time

def main():
    subreddit_input = input("Enter subreddits separated by + sign: ")
    subreddit_list = subreddit_input.split("+")
    print(fetch_content(subreddit_list))


if __name__ == "__main__":
    main()
