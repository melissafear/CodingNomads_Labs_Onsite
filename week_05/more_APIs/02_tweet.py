'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P

#https://tweepy.readthedocs.io/en/3.7.0/api.html
'''

import tweepy
import secrets

auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)


api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

api.update_status("Don't mind me, just testing the python tweepy package!")
