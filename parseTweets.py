__author__ = 'rahul'

import json
import re
import time


class ParseTweets:

    def __init__(self, results = None):
        if results == None:
            self.results = 'tweets.json'  # fall back file
        else:
            self.results = open(results)
        self.count = 0
        self.since_id = 10000000000000000000
        self.parsed_tweet = ''
        self.tweet = ''

    def parse(self):
        with open('parsed_tweets.json', 'w') as outfile:
            print '\nParsing initiated'
            for self.tweet in self.results.next():
                try:
                    tweet = json.loads(self.results.next())
                except:
                    pass
                if self.since_id != tweet['id']:
                    #print self.since_id, '--->', tweet['id']
                    data = {}
                    self.since_id = tweet['id']
                    data['tweet_id'] = tweet['id']
                    feed = tweet[u'text']
                    feed = re.sub(r'http://[\w.]+/+[\w.]+', " ", feed, re.IGNORECASE)    #remove http:// URL shortening links
                    feed = re.sub(r'https://[\w.]+/+[\w.]+'," ", feed, re.IGNORECASE)    #remove https:// URL shortening links
                    feed = re.sub('[@#$<>:%&]', ' ', feed)
                    data['tweet_text'] = feed
                    json.dump(data, outfile)
                    outfile.write('\n')
            self.progressBar()
            print '\nParsing complete, please read file for more information..'

    # A simple progress bar
    def progressBar(self):
        hash ="#."
        for i in range(10):
            time.sleep(1)
            print "%s"%(hash),

