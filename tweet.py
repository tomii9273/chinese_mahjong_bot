from __future__ import annotations
import tweepy
from random import randint
import sys


def get_one_tweet() -> tuple[str, int]:
    f = open("tweets.txt", "r", encoding="utf-8")
    lines = f.readlines()
    idx = randint(0, len(lines) - 1)
    one_tweet = lines[idx].replace("\n", "")
    return one_tweet, idx


def make_tweet():
    consumer_key = sys.argv[1]
    consumer_secret = sys.argv[2]
    access_token = sys.argv[3]
    access_token_secret = sys.argv[4]

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    tweet, idx = get_one_tweet()
    client.create_tweet(text=tweet)


if __name__ == "__main__":
    make_tweet()
