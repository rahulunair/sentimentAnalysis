sentimentAnalysis
=================

An application to show the sentiment of tweets using a search query and to displaying a graph of varying sentiment
over time. This is a context less application, which tokenizes each word in a tweet, and will use a NaiveBayes classifier
to classify the tweet as positive or negative.


Here this app have three classifiers, two of the classifiers use TextBlob modules built in classifiers, which in turn is
built from NLTK library. The third classifier is based on NLTK and a corpus of words that is attached here. This \
corpus(AFINN wordlist)can be downloaded form online as well.

After classifying each tweet a graph is plotted using matplotlib to show sentiment of tweets. Here if we use the 'Patterns
or the in house classifier then the classification will be very fast. But using the NaiveBayes classifier which has a lazy
classifier loading it will take around 2 seconds to classify.

The frontend has been creates using tkinter.

Modules used here are:

Textblob   -  https://textblob.readthedocs.org/en/dev/ an excellent text analysis module, you should take a look at it if
              you have to do any text based analysis or NLP.

NLTK       -  http://www.nltk.org/ , the natural language tool kit library.

Matplotlib -  This is a graphing library in python, using features of Matplotlib a dynamic graphic which rescales
              each time a newly classified tweet is obtained.

couchdb    -  A library to connect to the nosql database. This database is used to store the tweets

twitter    -  A library to connect to twitter using the twitter api

json       -  Module to parse json files

tkinter    -  A library to create graphical user interface

threading  -  A library to multi-thread the application gui and background process.


To run the application in commandline mode, go to the main.py and uncomment if __main__ == line and run the code
To run the application with gui just run it with no modifications run it.


This program uses two mechanisms to store the database files, one is used in analysis.py file to display count of tweets,
another call is done in tweettrek.py to save the tweets. Comment those two calls to the db and the program will work fine
without a couch db configuration.