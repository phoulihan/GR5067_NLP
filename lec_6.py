#!/usr/bin/env python
# coding: utf-8

# In[25]:


from bs4 import BeautifulSoup
import requests
import re

url = 'http://www.qmss.columbia.edu/faculty-and-staff'

content = requests.get(url)

soup = BeautifulSoup(content.text, 'html.parser')

tmp_text = [re.sub('[^A-z]+', ' ' ,word.text) for word in soup.findAll('p')]

tmp_text = ' '.join(tmp_text)

print(tmp_text)


# In[38]:


#pip install pyyaml ua-parser user-agents fake-useragent
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re

def fetch_urls(query, cnt):
    ua = UserAgent()
    
    google_url = 'https://www.google.com/search?q=' + query + "&num=" + str(cnt)
    try:
        response = requests.get(google_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.text, "html.parser")
        result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
        
        links = list()
        
        for r in result_div:
            try:
                link = r.find('a', href = True)
                if link != '':
                    print (link['href'])
                    links.append(link['href'])  
            except:
                pass
    except:
        print ("hey you")
        pass

    #now lets use the following function that returns
#URLs from an arbitrary regex crawl form google

#pip install pyyaml ua-parser user-agents fake-useragent
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re 

def fetch_urls(query, cnt):
    ua = UserAgent()

    #query = 'fishing'

    google_url = "https://www.google.com/search?q=" + query + "&num=" + str(cnt)
    try:
        response = requests.get(google_url, {"User-Agent": ua.random})
        soup = BeautifulSoup(response.text, "html.parser")

        result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})

        links = []
        titles = []
        descriptions = []
        for r in result_div:
            # Checks if each element is present, else, raise exception
            try:
                link = r.find('a', href = True)
                title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
                description = r.find('div', attrs={'class':'s3v9rd'}).get_text()

                # Check to make sure everything is present before appending
                if link != '' and title != '' and description != '': 
                    links.append(link['href'])
                    titles.append(title)
                    descriptions.append(description)
            # Next loop if one element is not present
            except:
                continue  
    except:
        pass
    
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa',l)
        clean_links.append(clean.group(1))
        
    return clean_links
    
temp = fetch_urls('fly fishing', 10)
print (temp)
    


# In[43]:


from nltk.corpus import stopwords

s_w = stopwords.words('english')
print (s_w)

sentence = 'the cat and the dog ran up the hill'

rem_sw = [word for word in sentence.split() if word not in s_w]
print (rem_sw)


# In[50]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

my_stemmer = PorterStemmer()

fun_sentence = 'running downing laughing the hill ran run unequal'

tmp = word_tokenize(fun_sentence)
tmp = ' '.join(tmp)

the_stem = [my_stemmer.stem(word) for word in fun_sentence.split()]

print (the_stem)

#for word in fun_sentence.split():
#    print (my_stemmer.stem(word))


# In[53]:


from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

doc1 = 'the brown fox jumped over the fence'
doc2 = 'the brown fox sat on the grass GRASS'

vectorizer = CountVectorizer()
my_vec = vectorizer.fit_transform([doc1, doc2])
#print (vectorizer.get_feature_names())
#print (my_vec.toarray())

my_pd = pd.DataFrame(my_vec.toarray())
my_pd.columns = vectorizer.get_feature_names()

my_pd.head()

from sklearn.feature_extraction.text import TfidfVectorizer


# In[55]:


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

my_vec = vectorizer.fit_transform([doc1, doc2])
#print (vectorizer.get_feature_names())
#print (my_vec.toarray())

import pandas as pd
my_pd = pd.DataFrame(my_vec.toarray())
my_pd.columns = vectorizer.get_feature_names()
print (my_pd.head())

