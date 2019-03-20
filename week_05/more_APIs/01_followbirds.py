'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import tweepy
import secrets
import pprint

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)


api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

my_followers = api.followers("gofearlessly")
str = str(my_followers[0])

#stripped = str.replace()

print(str)
