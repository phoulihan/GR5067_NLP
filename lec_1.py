# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:15:37 2019

@author: pathouli
"""

x_1 = 2
X_1 = 3

my_list = list()
my_list.append('a')
my_list.append('b')
my_list.append('c')

my_set = set()
my_set.add('a')
my_set.add('b')
my_set.add('c')
my_set.add('A')

my_dictionary = {'a_1': 1, 'b_a': 2}

my_new_list = list()
for word in my_list:
    my_new_list.append('word: ' + word)
    

my_new_list_inline = [('word: ' + word) for word in my_list]

my_new_list = list()
for word in my_list:
    if word != 'a':
        my_new_list.append('word: ' + word)

my_new_list_inline = [('word: ' + word) for word in my_list if word != 'a']

