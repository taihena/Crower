import os
import tweepy

print("bot has started")

CONSUMER_KEY = os.environ["CROWER_CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CROWER_CONSUMER_SECRET"]
ACCESS_KEY = os.environ["CROWER_ACCESS_KEY"]
ACCESS_SECRET = os.environ["CROWER_ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def publish_tweet(text):
    api.update_status(text)


publish_tweet("test")