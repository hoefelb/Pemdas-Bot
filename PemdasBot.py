#A simple twitter bot that evaluates mathmatical expressions when it is mentioned in a tweet.
#much thanks to pythonprogramming.net, where most of this code comes from
#source: https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/
#thanks to Tweepy for interfacing the code with Twitter's APIs
#source: https://github.com/tweepy/tweepy
#also thanks to r/python for finding a safe alternative to eval() for unsanitized data
#source: https://www.reddit.com/r/Python/comments/3r7e31/alternatives_to_eval_which_is_said_to_be_never/

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import ast


class Listener(StreamListener):
    def on_data(self,data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        tweet = tweet.replace('×','*')
        tweet = tweet.replace('x','*')
        tweet = tweet.replace('÷','/')
        tweet = tweet.replace('π','3.1415927')
        tweet = tweet.replace('^','**')
        username = all_data["user"]["screen_name"]
        print(tweet[11:])
        print(ast.literal_eval(tweet[11:]))
        result = str(ast.literal_eval(tweet[11:]))
        print(type(result))
        print (tweet)
        api = tweepy.API(auth)
        api.update_status("@"+username+" "+result)
        return True

    

    def on_error(self, status):
        print (status)
        print ("test")

#input authentication data here
#auth = tweepy.OAuthHandler('')
#auth.set_access_token('')

twitterStream = Stream(auth,Listener())
while (True):
    try:
        twitterStream.filter(track = ["@PEMDASBot"])
        api = tweepy.API(auth)
    except:
        print("Bad input")
