# get_old_tweets.py で取得した ID のツイートを削除するスクリプト

import sys
import time

import tweepy

# Twitter APIの認証情報
consumer_key = sys.argv[1]  # API Key
consumer_secret = sys.argv[2]  # API Key Secret
access_token = sys.argv[3]
access_token_secret = sys.argv[4]

# TweepyでAPIオブジェクトを作成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 対象のツイートIDを読み込む
with open("../tweet_archive/old_tweets_until_2022.txt", "r", encoding="utf-8") as f:
    tweet_ids = [line.strip() for line in f.readlines()]

print(tweet_ids[:10])
print("len(tweet_ids):", len(tweet_ids))

start_ind = 20801  # 途中で打ち切った場合に使う、開始インデックス

# ツイートを削除
for ind, tweet_id in enumerate(tweet_ids):
    if ind < start_ind:
        continue
    try:
        print(f"Deleting tweet ID {tweet_id} (index {ind})")
        api.destroy_status(tweet_id)
        time.sleep(0.5)  # APIの制限を避けるための遅延
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
        sys.exit()
