#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:21:23 2019

@author: kate moore
"""

from bs4 import BeautifulSoup
import requests
import re

# Sample URL
url = 'http://www.qmss.columbia.edu/faculty-and-staff'

# "requests.get" package "gets" the URL
content = requests.get(url)

# pulls the text from the object, "content", using a tool called "html.parser"
soup = BeautifulSoup(content.text, 'html.parser')
#print(soup)
#print(soup.title)

# Asks for everything between paragraph markers 'p'
tmp_text = soup.findAll('p')
#print(tmp_text)

# Clean-up the text
tmp_text = [word.text for word in tmp_text] # This will get ONLY text from the site
tmp_text = ' ' .join(tmp_text)
tmp_text = re.sub('[^A-z]+', ' ', re.sub('xa0', ' ', tmp_text))
print(tmp_text)

# Alternative, "cool" way to clean-up the text
tmp_text = [re.sub('[^A-z]+',  ' ', word.text) for word in soup.findAll('p')]
tmp_text = ' ' .join(tmp_text)
print(tmp_text)

# NOTE: LinkedIn, FB, and other sites will block you from pulling text from their sites

# REMINDER: To do URL crawling you have to install this package... 
# pip install pyyaml ua-parser user-agents fake-useragent

import requests
from fake_useragents import UserAgent
from bs4 import BeautifulSoup
import re

# Build a function
def fetch_urls(query, cnt):
    ua = UserAgent()
    
    # Reconstruct the Google Search Engine
    google_url = 'https://www.google.com/search?q=' + query + '&num=' + str(cnt)
    
    # A try, catch, block allows you to get around errors, ie. allows the program to continue despite errors
    try:
        # randomly generate User Agents. This helps you avoid getting blocked by Google
        response = requests.get(google_url, {User-Agent: ua.random})
        
        # this is the same line we used in the code above
        soup = BeautifulSoup(response.text, 'html.parser')

        # This is a special code the uses JavaScript (ZINbcc) to capture "hits" from the Google Search
        result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
        
        links = list()
       
        for r in result_div:
        
            try:
                link = r.find('a', href = True)
                
                if link != '':
                    print(link['href'])
                    links.append(link['href'])
                
            except:
                continue
    except:
        pass
        
    # This code is designed to clean up the links
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa',l)
        clean_links.append(clean.group(1))
        
    return clean_links

temp = fetch_urls('unicorns', 10)
print(temp)


'''
Class Activity:
    Crawl the 10 URLs from the output of fetch_urls and
    append the following to a DataFrame:
'''

# Answer not covered in class.
# It was suggested that the answer to this activity is a major part of HW2.



# STOP WORDS: relatively meaningless words
from nltk.corpus import stopwords

# Ask for a list of all the Stop Words in English
s_w = stopwords.words('english')
#print(s_w)

sentence = "I think unicorns shouldn't ride the subway."

rem_sw = [word for word in sentence.split() if word not in s_w]
print(rem_sw)


# STEMMING: remove the common morphological and inflexional endings from words
# in English for Information Retreval Systems
from nltk.stem import PorterStemmer

my_stemmer = PorterStemmer()

fun_sentence = 'ok but unicorns are really great and if they want to ride the subway I think they should be allowed to!'

for word in fun_sentence.split():
    print(my_stemmer.stem(word))

# Alternatively, you could use this more elegant way
tmp = word_tokenize(fun_sentence)
tmp = ' ' .join(tmp)
print(tmp)

# This will give you all the words as a list
the_stem = [my_stemmer.stem(word) for word in fun_sentence.split()]
#print(the_stem)



# VECTORIZE: Allows you to count the frequency of word occurance.
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

doc1 = 'the brown fox jumped over the fence'
doc2 = 'the brown fox sat in the grass'

vectorizer = CountVectorizer()
my_vec = vectorizer.fit_transform([doc1, doc2])
#print(vectorizer.get_feature_names())
#print(my_vec.toarray())

my_pd = pd.DataFrame(my_vec.toarray())
my_pd.columns = vectorizer.get_feature_names()

print(my_pd)

# NOTE: Vectorize forces text into lower case.



# TF-IDF: Term Frequency - Inverse Document Frequency
# This is directly proportional to the number of times a word occurs in the document
# AND it is inversely propotional to the number of times a word occurs across documents
# This weights words more heavily if they show-up frequently in the document AND across documents
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

doc1 = 'the brown fox jumped over the fence'
doc2 = 'the brown fox sat in the grass'

vectorizer = TfidfVectorizer()
my_vec = vectorizer.fit_transform([doc1, doc2])
#print(vectorizer.get_feature_names())
#print(my_vec.toarray())

my_pd = pd.DataFrame(my_vec.toarray())
my_pd.columns = vectorizer.get_feature_names()

print(my_pd)

# This might look better if you are using Spyder. It forces Syder to show all the rows.
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(my_pd)
