from TweetTruck import TweetTruck

'''
    Count the number of tweets in the database and display them one by one
'''
COUCH_DATABASE = 'tweets_db'

delivery = TweetTruck(COUCH_DATABASE)

print 'Number of tweets in the truck is:  %d\n' % delivery.count_tweets()

def getEm():
    '''
    call function to get the tweets stored in the database
    :return: A dictionary of tweets
    '''
    for doc in delivery.get_tweets():
        print '%s : %s\n' % doc.value['id'] ,doc.value['text']
    return delivery.get_tweets()


