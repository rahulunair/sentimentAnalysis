
__author__ = 'rahul'

import tweetTrek
import parseTweets

if __name__ == '__main__':
    #trekker = tweetTrek.TweetTrek("rahul")
    parser = parseTweets.ParseTweets("tweets.json")
    #trekker.trek()
    parser.parse()

