#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

the_data = np.array([1,5,7,8,9])

print (np.mean(the_data))

the_data_2d = np.array([(1,5,8,3), (4,7,8,9)])

print (the_data_2d)
print (np.transpose(the_data_2d))
print (the_data_2d.shape)


# In[7]:


#recall from last week
import os
import pandas as pd
the_path = 'C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/data/topics/'
the_dirs = os.listdir(the_path)
print (the_dirs)

the_files = os.listdir(the_path + the_dirs[0])
the_file_names = pd.DataFrame()
for word in the_files:
    the_file_names = the_file_names.append({'file_name': word, 'label': the_dirs[0]}, ignore_index=True)
    

#IN-CLASS EXERCISE; in lieu of the filename, do the same as above, but just read the text in
#and CLEAN it up, below is starter code to get you pointed in the right direction
import os
import pandas as pd
t_path = 'C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/data/topics/'

the_df = pd.DataFrame()
for dir_name in the_dirs:
    the_filenames = os.listdir(the_path + dir_name)
    for word in the_filenames:
        f = open(t_path + dir_name + '/' + word, "r", encoding='ISO-8859-1')
        tmp_read = str(f.read())#.encode('ISO-8859-1'))
        tmp = pd.DataFrame([tmp_read], columns=['body'])
        tmp['label'] = dir_name
        the_df = the_df.append(tmp, ignore_index=True)
        f.close()
print (the_df.head())


# In[10]:


import re

def clean(var):
    tmp = re.sub('[^A-z]+', ' ', var)
    return tmp

the_df['cleaned'] = the_df.body.apply(clean)
print (the_df.head())


# In[12]:


my_df_new_tmp_no_sw = pd.DataFrame(map(lambda x, y: (clean(x), y), the_df.body, the_df.label))
print (my_df_new_tmp_no_sw.head())
                                   


# In[14]:


from nltk.tokenize import word_tokenize

the_test = 'this class is lots of fun yeah'

the_tokenize = word_tokenize(the_test)

print (the_tokenize)


# In[23]:


from nltk.probability import FreqDist

the_sentence = 'abc abc b c d d f f f g h z z z'

my_freq_dist = FreqDist(the_sentence.split())

my_dictionary = dict(my_freq_dist)

print (my_dictionary)

t = 'a,b,c,d,d,d'
my_split = t.split(',')
print (my_split)


# In[31]:


the_sentence = 'abc ABC b B d d F F f g h z z Z'

#the_sentence = [word.lower() for word in the_sentence.split()]
the_sentence = the_sentence.lower().split()

my_freq_dist = FreqDist(the_sentence)

my_dictionary = dict(my_freq_dist)

print (my_dictionary)


# In[43]:


import nltk
#from nltk.book import *

the_books = nltk.corpus.gutenberg.fileids()

print (the_books)


# In[42]:


raw_text = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
#print (raw_text)
words_text = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
#print (words_text)
#print (len(words_text))
words_text = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')
print (words_text)
print (len(words_text))


# In[52]:


the_words = [word for word in raw_text,split() if word.isdigit() or word.isalpha()]
print (the_words[0:10])


# In[51]:


print (words_text[0:10])


# In[ ]:


import nltk
from nltk.book import *
import pandas as pd
import numpy as np
nltk.corpus.gutenberg.fileids()
the_books = nltk.corpus.gutenberg.fileids()

import re
import operator
the_data = pd.DataFrame()
for word_bk in the_books:
    raw = nltk.corpus.gutenberg.raw(word_bk)
    sent = nltk.corpus.gutenberg.sents(word_bk)
    the_words = nltk.corpus.gutenberg.words(word_bk)
    the_words = [word for word in the_words if word.isdigit() or word.isalpha()]
    freq = dict(FreqDist(the_words))
    top_five = sorted(freq, key=freq.get, reverse=True)[:5]
    top_five = ',' .join(top_five)
    bot_five = sorted(freq, key=freq.get, reverse=True)[-5:]
    bot_five = ',' .join(bot_five)
    word_count = [len(word) for word in sent]
    the_data = the_data.append({'book': word_bk, 
                                'aveWordPerSent': round(np.average(word_count), 2),
                                'medianWordPerSent': np.median(word_count),
                                'longestSentenceLength': np.max(word_count),
                                'shortestSentenceLength': np.min(word_count),
                                'topFiveOccWords': top_five,
                                'bottomFiveOccWords': bot_five}, ignore_index=True)

