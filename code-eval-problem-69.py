# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:14:46 2017

@author: jliu
"""

def get_indices(string):
    """inputs: a string
    returns: a dictionary with each unique character as a key and a list of
    the indices in which it occurs as the value
    """
    index_dict = {}
    for i in range(len(string)):
        if index_dict.get(string[i], -1) == -1:
            index_dict[string[i]] = [i]
        else:
            index_dict[string[i]].append(i)
    return index_dict

base, substr = "rabbbit,rabbit".split(",")
index_dict = get_indices(base)

count= 0
for i in range(len(substr)-1):
    next_letter = substr[i+1]
    for j in index_dict[substr[i]]:
        if next_letter != substr[1]:
            count -= 1
        for k in index_dict[next_letter]:
            if k > j:
                count += 1
                    
print(count)