#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_string = 'hello world!'


# In[2]:


print (my_string)


# In[3]:


import re


# In[26]:


my_string = 'a cat%% jumped# #over #the !!dog&*^'


# In[27]:


print (my_string)


# In[22]:


my_new_string = re.sub('[^A-z0-9]+', ' ', my_string)


# In[23]:


print (my_new_string)


# In[28]:


my_new_string = re.sub('[^a-zA-Z0-9]+', ' ', my_string) #way to remove special escape character from python


# In[29]:


print (my_new_string)


# In[49]:


my_string = 'a 7cat%% jumped# #over #the764 dog&*!!'


# In[45]:


my_new_string = re.sub('[^A-z! ]', '', my_string)


# In[47]:


print (my_new_string)


# In[50]:


re.findall('#', my_string)


# In[51]:


re.findall('ver', my_string)


# In[52]:


my_list = [1,2,4,6]


# In[53]:


for word in my_list:
    print(word)


# In[58]:


my_string = 'UDDDUDUDU'


# In[59]:


cnt = 0
for word in my_string:
    if word == 'U':
        cnt += 1
    else:
        cnt -= 1
print (cnt)


# In[72]:


the_string = 'UDDDUUUDDUUU'


# In[74]:


score = 0
t = 0
for word in the_string:
    if (word == 'U'):
        t += 1
    else:
        t -= 1
    if (t == 0) and (word == 'U'):
        score += 1


# In[75]:


def my_fun():
    print('hello world!')


# In[77]:


my_fun()


# In[78]:


def adder(a, b):
    the_out = a + b
    
    return the_out


# In[79]:


tmp = adder(34, 45)


# In[80]:


tmp


# In[81]:


def valley_counter(the_string):
    score = 0
    t = 0
    for word in the_string:
        if (word == 'U'):
            t += 1
        else:
            t -= 1
        if (t == 0) and (word == 'U'):
            score += 1
            
    return score


# In[82]:


tmp = valley_counter('UDDDUUUDDUUU')
print (tmp)


# In[83]:


the_dict = {'a': 1, 'b': 2, 'c': 3}


# In[85]:


the_dict['d']


# In[88]:


the_keys = ['a', 'b', 'c', 'd', 'a', 'b']


# In[89]:


for word in the_keys:
    tmp = the_dict[word]
    print (tmp)


# In[98]:


for word in the_keys:
    try:
        tmp = the_dict[word]
        print (tmp)
    except:
        print ("Hey Silly the key: " + word + " does NOT exist")
        pass


# In[99]:


the_ar = [1,4,4,4,5,6,7]
the_ar.count(4)


# In[100]:


the_wrd_ar = ['call', 'me', 'ishmael', 'yeah', 'call', 'me', 'me']


# In[101]:


the_wrd_ar.count('me')


# In[102]:


the_sentence = ' ' .join(the_wrd_ar)


# In[103]:


the_sentence


# In[104]:


tmp = len(re.findall('me', the_sentence))


# In[105]:


tmp


# In[106]:


tmp = len(re.findall('me', ' ' .join(the_wrd_ar)))


# In[107]:


re.findall('me', ' ' .join(the_wrd_ar))


# In[108]:


len(re.findall('me', ' ' .join(the_wrd_ar)))


# In[ ]:




