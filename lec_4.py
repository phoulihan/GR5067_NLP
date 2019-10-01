#!/usr/bin/env python
# coding: utf-8

# In[2]:


#nltk stop words
#what are stopwords? --> common terms, add little to no value to specific document classifications
from nltk.corpus import stopwords
import re
stop_words = set(stopwords.words('english'))

test = "my %text is very& ^*&messed up* and so (*^)"

#recall the text clean up code we created?
def clean_up(var):
    tmp = re.sub('[^a-zA-Z]+', ' ', var)
    return tmp


print (clean_up(test))

#recall the text clean up code we created?
def clean_up_sw(var):
    tmp = re.sub('[^a-zA-Z]+', ' ', var)
    tmp = [word for word in tmp.split() if word not in stop_words]
    tmp = ' '.join(tmp)
    return tmp

print (clean_up_sw(test))


# In[3]:


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
    
print(the_file_names.head())


# In[4]:


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


# In[6]:


#how about a lambda function to do it all in one swoop?
my_df_new_tmp_no_sw = pd.DataFrame(map(lambda x, y: (clean_up(x), y), the_df.body, the_df.label))
print (my_df_new_tmp_no_sw)


# In[ ]:




