# i've used nltk's stopwords and word_tokenize here
# other alternatives are to use str.translate() (import string) 
# like this: translator = str.maketrans("", "", string.punctuation)
# or: sklearn’s Built-in Pipeline: 
#  from sklearn.feature_extraction.text import TfidfVectorizer
# or use spaCy

import re
import nltk
from nltk.tokenize import word_tokenize

STOPWORDS = {
    "the", "is", "and", "to", "of", "in", "for", "on",
    "with", "as", "at", "by", "an", "be", "this", "that",
    "from", "it", "are", "was", "were", "or", "but"
}

def tokenize(text):
    #converts text to lowercase
    #extracts only alphabetic words using regex
    #returns list of tokens

    text = text.lower()

    # find all alphabetic sequences
    tokens = re.findall(r"[a-z]+", text)
    return tokens

def remove_stopwords(tokens):
    #removes common stopwords and short words

    filtered = [
        word for word in tokens
        if word not in STOPWORDS and len(word) > 2
    ]
    return filtered

def clean_text(text):
    #full preprocessing pipeline:
    # tokenize → remove stopwords
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)

    return tokens #return list, not string
