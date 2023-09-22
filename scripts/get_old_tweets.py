# 古いツイート (2022 年以前かつ「【」で始まる) の ID を取得するスクリプト

import json
from datetime import datetime

# tweet.jsの読み込み
with open(
    "../tweet_archive/twitter-2023-09-19-1a4929ba57c651124898036693f3e0133b7971e022768cbe536c32c608716f25/data/tweets.js",
    "r",
    encoding="utf-8",
) as f:
    content = f.read()

# "window.YTD.tweet.part0 = " の部分を取り除いてJSONとして解析
json_str = content.split("window.YTD.tweets.part0 = ")[1]
print(json_str[:20])
tweets_data = json.loads(json_str)
print(tweets_data[:2])

# 各ツイートからIDと日時を取り出す

with open("../tweet_archive/old_tweets_since_202301_until_202303.txt", "w", encoding="utf-8") as f:
    for tweet in tweets_data:
        # print(tweet.keys())
        tweet_id = tweet["tweet"]["id"]
        first_char = tweet["tweet"]["full_text"][0]
        created_at = datetime.strptime(tweet["tweet"]["created_at"], "%a %b %d %H:%M:%S %z %Y")
        # print(f"Tweet ID: {tweet_id}, Created At: {created_at}")
        if created_at.year == 2023 and created_at.month <= 3 and first_char == "【":
            print(f"Tweet ID: {tweet_id}, Created At: {created_at}")
            f.write(f"{tweet_id}\n")
