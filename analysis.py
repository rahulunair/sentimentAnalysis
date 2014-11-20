''' code to gather sentiment score of individual tweets
    use w_scored_tweets to get sentiment from inhouse tools
    use p_scored_tweets to get sentiment generated from patterns library.
'''


__author__ = 'rahul'

from textblob import TextBlob
import nltk
import scores
import json

file_name = 'parsed_tweets.json'
words = ''
w_scored_tweets = {}
p_scored_tweets = {}

def score_them():
    weighted_sentiment = scores.get_scores()
    tweets = open(file_name)
    count = 0
    counter = 0

    for line in tweets:

        try:
            tweet = json.loads(line)
            words = nltk.word_tokenize(tweet['tweet_text']) # removing tweets less than 5 words
            score = 0
            if len(words) > 5:
                for word in words:
                    word = str(word.lower())

                    # A weighted classifier
                    if word in weighted_sentiment:
                        count = count + 1
                        score += weighted_sentiment[word]
                        tweet['score'] = score
                        w_scored_tweets['count'] = count
                        w_scored_tweets['sentiment'] = score

                # Patterns classifier
                counter += 1
                blob = TextBlob(tweet[u'tweet_text'])
                sentiment = round(blob.sentiment[0], 3)
                p_scored_tweets['count'] = counter
                p_scored_tweets['sentiment'] = sentiment
                sentiment_pair = (w_scored_tweets, p_scored_tweets)
                print  sentiment_pair[1]


        except:
            pass
    return




#score_them() for testing purposes

