import tweepy
import keys
import copypasta
import os
import datetime


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def client():
    return tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret,
                         keys.access_token, keys.access_token_secret)


def tweet(api: tweepy.API, image_path: str):
    api.update_status_with_media("", image_path)
    datetime_now = datetime.datetime.now()
    str_format = "%Y%b%d %H:%M:%S"
    formatted_datetime = datetime_now.strftime(str_format)
    print(f"Tweeted successfully @ {formatted_datetime}")


def get_latest_tweet_id(api: tweepy.API):
    print(api.user_timeline(screen_name="morning_neru", count="1")[0].id)


if __name__ == "__main__":
    api = api()
    tweet(api, "morning.png")
