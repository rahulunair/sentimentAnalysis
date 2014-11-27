__author__ = 'rahul'
import json
import time
import twitter
from TweetStore import TweetStore


RANGE = 1
COUNT = 10

class TweetTrek:

    def __init__(self, search_term='interstellar'):

        self.api_key = 'j9AYP6RAGotmwg6v8IwVbw3j1'
        self.api_secret = 'c4b3KLEzdHilCOG5q9mbGboGOyHx4A1TiNvd3SR6DTAvc4TEqx'
        self.access_token_key = '52697739-SHrDzs5fSwWBpeO046OrUnVqDOTsaB0pjoeIxjvjw'
        self.access_token_secret = 'DDWDrcJPGX8jCo4NZgKEArhX3NPsdd8uvkMvjZ09TSRbB'
        self.since_id = 10000000000000000000
        self.api = twitter.Api(self.api_key, self.api_secret, self.access_token_key, self.access_token_secret)
        self.search_term = search_term  # tweet term

    def trek(self):

        DB = TweetStore("tweets_db")

        with open('tweets.json', 'w') as outfile:
            for i in range(0, RANGE):
                time.sleep(5)  # don't piss off twitter
                print 'since_id=', self.since_id, ', twitter loop', i
                #results = self.api.GetSearch(self.search_term, count=100, since_id=self.since_id)
                results = self.api.GetSearch(self.search_term, count=COUNT, max_id=self.since_id)
                # outfile.write('[')
                for tweet in results:
                    tweet = str(tweet).replace('\n', ' ').replace('\r', ' ')  # remove new lines
                    tweet = (json.loads(tweet))
                    if u'lang' in tweet and tweet[u'lang'] == 'en' and u'text' in tweet:
                        self.since_id = tweet['id']  # redefine since_id
                        print self.since_id
                        json.dump(tweet, outfile)
                        outfile.write('\n')  # print tweets on new lines
                        DB.save_tweet(tweet) # saving tweets in database
        return 1