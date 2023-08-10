def count_full_width_chars(s: str) -> int:
    """全角文字の数を返す"""
    return sum(int(ord(c) > 0x7F) for c in s)


def count_half_width_chars(s: str) -> int:
    """半角文字の数を返す"""
    return sum(int(ord(c) <= 0x7F) for c in s)


def check_tweet_char_limit(tweet: str) -> bool:
    """ツイートの文字数制限を満たしているかを返す"""
    return count_half_width_chars(tweet) + count_full_width_chars(tweet) * 2 <= 280


def test_tweet_char_limit():
    """tweets.txt のすべての行がツイートの文字数制限を満たしているかどうかを確認"""
    with open("tweets.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            assert check_tweet_char_limit(line.replace("\n", ""))
