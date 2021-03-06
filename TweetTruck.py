import couchdb
import couchdb.design


COUCH_SERVER = 'http://127.0.0.1:5984/'


class TweetTruck(object):
    '''
    database class to save, retrieve and count the number of tweets. Go to http://localhost:5984/_utils/index.html for a front end view of the db
    '''

    def __init__(self, dbname, url=COUCH_SERVER):
        try:
            self.server = couchdb.Server(url=url)
            self.db = self.server.create(dbname)
            self._create_views()
        except couchdb.http.PreconditionFailed:
            self.db = self.server[dbname]

    def _create_views(self):
        count_map = 'function(doc) { emit(doc.id, 1); }'
        count_reduce = 'function(keys, values) { return sum(values); }'
        view = couchdb.design.ViewDefinition('tweets', 'count_tweets', count_map, reduce_fun=count_reduce)
        view.sync(self.db)

        get_tweets = 'function(doc) { emit(("0000000000000000000"+doc.id).slice(-19), doc); }'
        view = couchdb.design.ViewDefinition('tweets', 'get_tweets', get_tweets)
        view.sync(self.db)

    def save_tweet(self, tw):
        tw['id'] = tw['text']
        self.db.save(tw)

    def count_tweets(self):
        for doc in self.db.view('tweets/count_tweets'):
            return doc.value

    def get_tweets(self):
        return self.db.view('tweets/get_tweets')

    def delete_tweets(self):
        self.db.delete()