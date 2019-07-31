import pandas as pd
from collections import Counter
from functools import reduce
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.csv', encoding="utf8")

# Extract column year
movies["year"] = movies["title"].apply(lambda x: x[-5:-1])
movies["year2"] = movies["title"].apply(lambda x: x[-6:-2] if x.endswith(" ") else x[-5:-1] )#if isinstance(x[-6:-2], int) is True else "unknown")
#print(movies["year2"])

cotnam = movies.year2.unique()
cottheloaitheophim = movies.genres.apply(lambda x: x.split('|'))
cotcacphim =  [item for sublist in cottheloaitheophim for item in sublist]
uniqListphim = reduce(lambda x,y: x+[y] if not y in x else x, cotcacphim,[])



# print(movies.year.unique())
# print(cotcacphim)
# print(uniqListphim)




# Select movie in year 1995
movies_1995 = movies[movies.year == '1995']

pd.options.mode.chained_assignment = None
# See this https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
genres_list = movies["genres"].apply(lambda x: x.split('|'))
print(genres_list)

flat_list = [item for sublist in genres_list for item in sublist]
#print(flat_list)
'''
#https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
flat_list = []
for sublist in l:
    for item in sublist:
        flat_list.append(item)
'''

# Count genres element
counter_genres = Counter(flat_list)
print(counter_genres)
# https://vimentor.com/vi/lesson/10-loc-du-lieu-trong-pandas



datacanve = pd.DataFrame.from_dict(counter_genres, orient='index').reset_index()
#print(counter_genres)
# Print most common genres
#print(counter_genres.most_common(1))
#print(datacanve)



datacanve.plot.line( x = 'index')
tick_labels = tuple(datacanve['index'])
x_max = int(max(plt.xticks()[0]))  # int() to convert numpy.int32 => int
# manually set you xtick labels
plt.xticks(range(0, x_max + 1), tick_labels, rotation=45)
# plt.show()

# 2. Vẽ biểu đồ line chart mô tả độ phổ biến của thể loại film
