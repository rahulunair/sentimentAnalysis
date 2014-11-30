''' code to gather sentiment score of individual tweets
    use w_scored_tweets to get sentiment from inhouse tools
    use p_scored_tweets to get sentiment generated from patterns library.
'''
import gettweets
import tweetTrek


__author__ = 'rahul'

from textblob import TextBlob
import nltk
import scores
import json
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt
import numpy
from DynamicGraph import DynamicGraph

file_name = 'parsed_tweets.json'
words = ''
w_scored_tweets = {}
p_scored_tweets = {}
graph_xdata = []
graph_ydata = []
dyna_g = DynamicGraph()


def score_them():
    '''
    Takes in tweets with length with more than 5 letters, and classifies the tweets and calculate the sentiment of
    tweet. It has three classifiers, a weighted sentiment classifier, a patterns classifier, and Naivebayes classifier.

    :return: accumilated_sentiment integer value
    '''

    gettweets.count()  # Total number of tweets in database, comment if no database is configured
    weighted_sentiment = scores.get_scores()
    tweets = open(file_name)
    count = 0
    counter = 0

    for line in tweets:

        try:
            tweet = json.loads(line)
            words = nltk.word_tokenize(tweet['tweet_text'])  # removing tweets less than 5 words
            score = 0
            if len(words) > 5:
                for word in words:
                    word = str(word.lower())

                    # A weighted classifier
                    if word in weighted_sentiment:
                        count = count + 1
                        score += weighted_sentiment[word]
                        tweet['score'] = score
                        w_scored_tweets[count] = score  # count: sentiment

                '''
                # Patterns classifier
                counter += 1
                blob = TextBlob(tweet[u'tweet_text'])
                sentiment = round(blob.sentiment[0], 3)
                p_scored_tweets[counter] = sentiment       # count: sentiment
                sentiment_pair = (w_scored_tweets, p_scored_tweets) # weighted and pattern based sentiment analysis
                '''

                # Naview Bayes classifier based on movie reviews dataset from NLTK library
                counter += 1
                blob = TextBlob(tweet[u'tweet_text'], analyzer=NaiveBayesAnalyzer())
                if blob.sentiment[1] > 0.51:
                    senti_score = blob.sentiment[1]
                else:
                    senti_score = -blob.sentiment[2]
                sentiment = round(senti_score, 3)
                p_scored_tweets[counter] = sentiment  # count: sentiment
                sentiment_pair = (w_scored_tweets, p_scored_tweets)  # weighted and pattern based sentiment analysis
                graph_xdata.append(counter)
                graph_ydata.append(sentiment)
                dyna_g.on_running(graph_xdata, graph_ydata)
                print graph_xdata, " ", graph_ydata
        except:
            pass
    accumulated_sentiment = sum(p_scored_tweets.values()) / len(p_scored_tweets)
    print accumulated_sentiment
    return accumulated_sentiment


def update_line(graph, counter, sentiment):
    graph.set_xdata(numpy.append(graph.get_xdata(), counter))
    graph.set_ydata(numpy.append(graph.get_ydata(), sentiment))
    plt.draw()
    print graph.get_xdata(), graph.get_ydata()


# score_them() for testing purposes

