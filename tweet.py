import sys
import time
from random import randint

import tweepy


def get_one_tweet() -> tuple[str, int]:
    """ツイート一覧からランダムに 1 ツイートを取得し、index とともに返す"""
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

    n_set = 5
    n_retry = 5
    # 5回試すのは、12時間以内 (直近4ツイート) の重複制限を確実に回避するため。
    # 2025年12月頃から失敗 (403エラー。X側のスパム対策強化？) が増えたので回数を増やしたがそれでも連続で失敗したので、2分間空けて5セット試すことにした。

    for s in range(n_set):
        print(f"set {s} start")
        for t in range(n_retry):
            while idx in ng_idx:
                tweet, idx = get_one_tweet()
            try:
                client.create_tweet(text=tweet)
                print(f"set {s} tweet {t} succeeded (idx: {idx})")
                return
            except tweepy.TweepyException as e:
                print(f"set {s} tweet {t} failed (idx: {idx})")
                print(f"reason: {e}")
                ng_idx.append(idx)
                time.sleep(1)
        time.sleep(120)

    raise MaxRetriesExceededError()


if __name__ == "__main__":
    make_tweet()
