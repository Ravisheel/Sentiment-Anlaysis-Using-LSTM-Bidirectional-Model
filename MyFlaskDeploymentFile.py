# -*- coding: utf-8 -*-
"""
Created on Mon January 9 16:17:13 2023

@author: Ravi Sheel
"""

import tensorflow as tf
import re

from flask import Flask, request,render_template
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from keras.models import load_model


model = load_model('lstm_bid_model_90acc.h5')


with open('tokenizer.pickle', 'rb') as token:
    tokens = pickle.load(token)
    

fun = Flask(__name__)


eng_stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
regex = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

def cleaning(sen, lem=True):
    sen = re.sub(r'\d+', '', sen)
    sen = re.sub(regex, ' ', str(sen).lower()).strip()
    sen_list = []
    for token in sen.split():
        if token not in eng_stopwords:
            if lem:
                sen_list.append(lemmatizer.lemmatize(token))
            else:
                sen_list.append(token)
    return " ".join(sen_list)

@fun.route('/')
def home():
    return render_template('test.html')



@fun.route('/predict',methods=['POST'])
def predict():
    
    text = [str(x) for x in request.form.values()]
    
    sentiment = ['Negative', 'Neutral', 'Positive']

    text_list = []
    for sen in text:
        cleaned = cleaning(sen)
        text_list.append(cleaned)
        
    tokenizer = tokens.texts_to_sequences(text_list)
    
    pads = pad_sequences(tokenizer, padding='post', maxlen=50)
    
    query_sentiments = model.predict(pads).argmax(axis=1)
    
    return render_template('test.html', prediction_text= f"The predicted sentence sentiment is: {sentiment[query_sentiments[0]]}")

if __name__ == "__main__":
    fun.run(debug=False)


