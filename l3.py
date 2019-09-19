#!/usr/bin/env python
# coding: utf-8

# In[1]:


set_a = set(['blue', 'green', 'violet', 'red'])
set_b = set(['green', 'yellow', 'blue', 'orange'])

set_a & set_b #intersection


# In[2]:


set_a | set_b


# In[3]:


set_a - set_b


# In[4]:


set_a^set_b


# In[6]:


from datetime import *
the_datetime = datetime.now()
print (the_datetime)


# In[7]:


the_year = the_datetime.year
print (the_year)


# In[8]:


print (the_datetime.strftime("%B"))


# In[9]:


print (the_datetime.strftime("%b"))


# In[10]:


print (the_datetime.strftime("%A"))


# In[11]:


print (the_datetime.strftime("%a"))


# In[13]:


print (the_datetime.strftime('%Y%m%d'))


# In[23]:


print (the_datetime.strftime('%Y%m/%d %H:%M:%S'))


# In[15]:


str_date = '2019-09-18 15:54:22'


# In[20]:


str_date_conv = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print (str_date_conv)
print (type(str_date_conv))


# In[21]:


print(str_date_conv.year)


# In[24]:


import pandas as pd


# In[25]:


my_df = pd.DataFrame({'int_a': [1,2,3,4,5], 'int_b': [12,14,16,18,20]})


# In[26]:


print (type(my_df))


# In[27]:


my_df.head()


# In[30]:


print (list(my_df.index))


# In[32]:


my_df.head(1)


# In[33]:


my_df.tail(1)


# In[64]:


the_data = pd.read_csv('C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/data/l3_ex.csv')
the_data = the_data.append({'c1': 6, 'c2': 'z', 'c3': 0.0315}, ignore_index=True)
the_data = pd.concat([the_data, pd.DataFrame({'c4': [1,2,3,4,5,6,7,8,9,10,11]})], axis=1)#col concat

print (the_data)


# In[35]:


the_data.head()


# In[50]:





# In[49]:


the_data.head()


# In[66]:


#lambda
x_a = (lambda x: x*x)
the_answer = x_a(2)
print (the_answer)


# In[67]:


x_b = (lambda x, y: x*y)
the_answer = x_b(4,5)
print (the_answer)


# In[85]:


the_data = pd.read_csv('C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/data/l3_ex.csv')
the_data = the_data.append({'c1': 6, 'c2': 'z', 'c3': 0.0315}, ignore_index=True)
the_data_new = pd.DataFrame(map(lambda x: (x, x*2), the_data.c1))
#print (the_data_new)

the_data_filt = pd.DataFrame(filter(lambda x: (x >= 4), the_data.c1))
#print (the_data_filt)

from functools import reduce
the_ar = [1,2,3,4,5]
the_data_red = reduce(lambda x, y: (x + y), the_ar)
#print (the_data_red)
print (sum(the_ar))


# In[98]:


f = open(r'C:\Users\pathouli/myStuff\academia\columbia\socialSciences\GR5067\lectures\l3\example_text.txt', 'r')
the_read = f.read()
print (the_read)
#for line in f:
#    print (line, end='')
#    print ("test")
#the_read_ar = f.readlines()
#print (the_read_ar)
f.close()


# In[103]:


import os
the_path = 'C:/Users/pathouli/myStuff/academia/columbia/socialSciences/GR5067/data/topics/'
the_dirs = os.listdir(the_path)
print (the_dirs)


# In[110]:


the_files = os.listdir(the_path + the_dirs[0])
the_file_names = pd.DataFrame()
for word in the_files:
    the_file_names = the_file_names.append({'file_name': word, 'label': the_dirs[0]}, ignore_index=True)
    
print(the_file_names)


# In[ ]:




