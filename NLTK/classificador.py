import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

nltk.download('movie_reviews')

neg_reviews = [(movie_reviews.words(file_id), 'negative') for file_id in movie_reviews.file_ids('neg')]
pos_reviews = [(movie_reviews.words(file_id), 'positive') for file_id in movie_reviews.file_ids('pos')]

reviews = neg_
