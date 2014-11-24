
__author__ = 'rahul'


import tweetTrek
import parseTweets
import scores
import sys
from analysis import score_them

print sys.path


if __name__ == '__main__':
    trekker = tweetTrek.TweetTrek("test")
   # parser = parseTweets.ParseTweets("tweets.json")
    trekker.trek()
   # parser.parse()
    #for key, value in scores.get_scores().items():
    #scoreTweets
    #sentiment = score_them()



