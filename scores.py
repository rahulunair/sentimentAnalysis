
def get_scores(file = 'sentiment.txt'):
    '''
    :param file: File with tokenized and weighted sentiment.
    :return: Returns a dictionary of the same file
    '''
    SHS= open(file) # Simulated Human Sentiment # AFINN_1 score
    weighted_sentiment = {}
    for line in SHS:
        term, score = line.split("\t")
        weighted_sentiment[term] = int(score)
    return weighted_sentiment
