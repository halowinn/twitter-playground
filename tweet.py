import tweepy
import time

consumer_key = '8zKYjx5e8lhm23jEYpiV5V2kw'
consumer_secret = 'UGfCnrwZWcXxBbxZeK6VmdRrNllyKUD4P4rbFsU42mbUSqlT9X'
access_token = '3703164074-j990GXJ59E3DXruMuYcxVOcNPSRHJoIJmgDqNUA'
access_token_secret = 'JHAPaOe2sn3zZwM1MqXTwxSezxZKVmK2CuHWCSfkvTBId'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


search_string = 'python'
numberofTweets = 2

# for tweet in limit_handle(tweepy.Cursor(api.search, search_string).items(numberofTweets)):
#     try:
#         tweet.favorite()
#         print('I liked the tweet')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

# Follower bot
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'kirbs':
        follower.follow()
        break
