__author__ = 'rahul'

import json


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
            print 'Parsing initiated'
            for self.tweet in self.results.next():
                try:
                    tweet = json.loads(self.results.next())
                except:
                    pass

                if self.since_id != tweet['id']:
                    print self.since_id, '--->', tweet['id']
                    data = {}
                    self.since_id = tweet['id']
                    data['tweet_id'] = tweet['id']
                    data['tweet_text'] = tweet[u'text']
                    json.dump(data, outfile)
                    outfile.write('\n')
            print 'Parsing complete, please read file for more infomation..'
