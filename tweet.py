from __future__ import annotations
import tweepy
from random import randint
import sys
import time


def get_one_tweet() -> tuple[str, int]:
    f = open("tweets.txt", "r", encoding="utf-8")
    lines = f.readlines()
    idx = randint(0, len(lines) - 1)
    one_tweet = lines[idx].replace("\n", "")
    return one_tweet, idx


class MaxRetriesExceededError(Exception):
    pass


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

    ng_idx = [-1]  # 一度試して失敗したツイート番号を入れる
    idx = -1

    max_retries = 5  # 5 回試せば 12 時間以内 (直近 4 ツイート) の重複制限は回避可能

    for t in range(max_retries):
        while idx in ng_idx:
            tweet, idx = get_one_tweet()
        try:
            client.create_tweet(text=tweet)
            return
        except tweepy.TweepyException as e:
            print(f"tweet {t} failed (idx: {idx})")
            print(f"reason: {e}")
            ng_idx.append(idx)
            time.sleep(1)

    raise MaxRetriesExceededError()


if __name__ == "__main__":
    make_tweet()
