# get_old_tweets.py で取得した ID のツイートを削除するスクリプト

import sys
import time

import requests
from requests_oauthlib import OAuth1Session

# X API の認証情報
consumer_key = sys.argv[1]  # API Key
consumer_secret = sys.argv[2]  # API Key Secret
access_token = sys.argv[3]
access_token_secret = sys.argv[4]

# OAuth 1.0a で認証するセッションを作成
session = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# 対象のツイートIDを読み込む
with open(
    "../tweet_archive/old_tweets_since_202301_until_202303.txt", "r", encoding="utf-8"
) as f:
    tweet_ids = [line.strip() for line in f.readlines()]

print(tweet_ids[:10])
print("len(tweet_ids):", len(tweet_ids))

start_ind = 0  # 途中で打ち切った場合に使う、開始インデックス

# ツイートを削除
for ind, tweet_id in enumerate(tweet_ids):
    if ind < start_ind:
        continue
    try:
        print(f"Deleting tweet ID {tweet_id} (index {ind})")
        response = session.post(
            f"https://api.twitter.com/1.1/statuses/destroy/{tweet_id}.json",
            timeout=60,
        )
        response.raise_for_status()
        time.sleep(0.5)  # APIの制限を避けるための遅延
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit()
