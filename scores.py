__author__ = 'rahul'

def get_scores(file = 'sentiment.txt'):
    SHS= open(file) # Simulated Human Sentiment # AFINN_1 score
    valued_sentiment = {}
    for line in SHS:
        term, score = line.split("\t")
        valued_sentiment[term] = int(score)
        return valued_sentiment
