import pandas as pd
from functools import reduce
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

stop = ["","i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
movies = pd.read_csv("movies.csv")
pd.options.mode.chained_assignment = None
title_list = movies["title"].apply(lambda x: x.replace(x[-6:], '').split(' '))
title_keylist = title_list.apply(lambda x: [item for item in x if item not in stop])
# print(title_list)
# print(title_keylist)
flat_listkey = [item for sublist in title_keylist for item in sublist]
#print(flat_listkey)
# Count genres element
counter_title = Counter(flat_listkey)
print(counter_title)
print(counter_title.most_common(10))

'''
#https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)
'''


