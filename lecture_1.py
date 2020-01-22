#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Lecture 1 Code Examples


# In[ ]:


a = 1
b = 2

c = a*b


# In[5]:


print (c)


# In[8]:


#instantiate list with values
my_list = [1,2,3,4,5]


# In[7]:


#type is a keyword that returns the datatype
type(my_list)


# In[9]:


my_list


# In[14]:


#instantiation of a list
my_list = list()
#add an item to the list
my_list.append(1)
my_list
my_list.append(5)


# In[15]:


#len is a keyword and returns the length, i.e. number of items in array
len(my_list)


# In[16]:


my_list


# In[17]:


#indexing in python starts at 0
my_list[1]


# In[18]:


my_list[0]


# In[19]:


my_list.append(0.123)


# In[20]:


#note: multiple datatypes, interger, float, string, etc can be added to array
my_list


# In[21]:


my_list.append(True)
my_list.append('hello world')
my_list


# In[23]:


#instantiate a set, set is just like a like but only unique values, case sensitive
my_set = set()
my_set.add('patrick')
my_set.add('kate')
my_set.add('patrick')
my_set.add('Patrick')
my_set


# In[26]:


#hard coded dictionary
my_dict = {'patrick': 3.9, 'kate': 4.0}


# In[27]:


my_dict


# In[28]:


#retrieve value by passing key
my_dict['patrick']


# In[29]:


#retrieve dictionary keys
my_dict.keys()


# In[30]:


#retrieve dictionary values
my_dict.values()


# In[31]:


#loop statement
for word in my_dict.keys():
    print (my_dict[word])


# In[34]:


cnt_dict = dict()
for i in range(0,10):
    cnt_dict[i] = i*2
    #print(cnt_dict[i])
    
cnt_dict


# In[38]:


#while statement, continue until condition is met
i = 0
while i < 10:
    i=i+1
    #print(i)


# In[51]:


import pandas as pd
#pandas dataframe
my_pd = pd.DataFrame()

#appending a pandas dataframe
for i in range(0,10):
    my_pd = my_pd.append({'name': i, 'grade': int(i+20), 'string': str(i)}, ignore_index=True)

my_pd


# In[57]:


#sum columns (axis=0), sum across rows (axis=1)
print (my_pd.sum(axis=0))
print (my_pd.sum(axis=1))


# In[49]:


#standard deviation across rows
my_pd.std(axis=1)


# In[58]:


#concatente 2 dataframes together (must be same number of columns)
pd.concat([my_pd, my_pd])


# In[ ]:




