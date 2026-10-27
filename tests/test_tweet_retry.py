import unittest
from unittest.mock import Mock, patch

import requests

import tweet


class TweetRetryTest(unittest.TestCase):
    def test_投稿が拒否されたら別の候補で再試行する(self):
        client = Mock()
        client.create_tweet.side_effect = [requests.HTTPError(), {"data": {"id": "1"}}]
        with (
            patch(
                "tweet.sys.argv", ["tweet.py", "consumer", "secret", "token", "secret"]
            ),
            patch("tweet.XClient", return_value=client),
            patch("tweet.get_one_tweet", side_effect=[("候補1", 1), ("候補2", 2)]),
            patch("tweet.time.sleep"),
        ):
            tweet.make_tweet()
        self.assertEqual(client.create_tweet.call_count, 2)
        client.create_tweet.assert_called_with(text="候補2")
