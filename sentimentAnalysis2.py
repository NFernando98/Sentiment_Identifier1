import numpy as np
import pandas as pd
from textblob import TextBlob

import re
import nltk



def get_emotion(sentence):
    """
    Returns the emotion of a sentence as a string
    """
    blob = TextBlob(sentence)
    print(blob.sentiment)
    print(blob.words)
    
    sentiment = blob.sentiment.polarity
    if sentiment > 0.5:
        return 'happy'
    elif sentiment > 0:
        return 'content'
    elif sentiment < -0.5:
        return 'angry'
    elif sentiment < 0:
        return 'sad'
    else:
        return 'neutral'


newSentence = input("Send a message: ")
print(get_emotion(newSentence))



