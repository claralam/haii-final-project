from routes import configure_routes
from flask import Flask


# Importing packages
import numpy as np
import pandas as pd
import sklearn
import imblearn
import string
import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

from sklearn.base import TransformerMixin

app = Flask(__name__)

if __name__ == '__main__':
    # List of punctuations
    # Create our list of punctuation marks
    punctuations = string.punctuation

    # Create our list of stopwords
    nlp = spacy.load('en_core_web_sm')
    stop_words = spacy.lang.en.stop_words.STOP_WORDS

    # Load English tokenizer, tagger, parser, NER and word vectors
    parser = English()

    # Rewritten tokenizer function
    def spacy_tokenizer(sentence):
        # Creating our token object, which is used to create documents with linguistic annotations.
        mytokens = parser(sentence)

        new_mytokens = []
        # Lemmatizing each token and converting each token into lowercase
        for word in mytokens:
            word_str = str(word)
            if word_str not in stop_words and word_str not in punctuations:
                doc = nlp(word_str)
                if doc[0].lemma_ != "-PRON-":
                    new_mytokens.append(doc[0].lemma_.lower().strip())
                else:
                    new_mytokens.append(doc[0].lower_)

        # return preprocessed list of tokens
        return new_mytokens

    # Further cleaning of text data
    class predictors(TransformerMixin):
        def transform(self, X, **transform_params):
            # Cleaning Text
            cleaned = [clean_text(text) for text in X]
            return cleaned

        def fit(self, X, y=None, **fit_params):
            return self

        def get_params(self, deep=True):
            return {}

    def clean_text(text):
        return text.strip().lower()

    configure_routes(app)
    app.run(host="0.0.0.0", debug=True, port=80)
