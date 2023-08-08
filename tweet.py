import sys
from random import randint

import tweepy


def get_one_tweet() -> str:
    f = open("tweets.txt", "r", encoding="utf-8")
    lines = f.readlines()
    idx = randint(0, len(lines) - 1)
    one_tweet = lines[idx].replace("\n", "")
    return one_tweet


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
    tweet = get_one_tweet()
    client.create_tweet(text=tweet)


if __name__ == "__main__":
    make_tweet()
