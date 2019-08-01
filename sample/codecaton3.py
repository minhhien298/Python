import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv("movies.csv")
pd.options.mode.chained_assignment = None
genres_list = movies["genres"].apply(lambda x: x.split('|'))
flat_list = [item for sublist in genres_list for item in sublist]
counter_genres = Counter(flat_list)

#https://stackoverflow.com/questions/29233283/plotting-multiple-lines-with-pandas-dataframe
movies["year"] = movies["title"].apply(lambda x: x[-6:-2] if x.endswith(" ")  else x[-5:-1] )#if isinstance(x[-6:-2], int) is True else "unknown")
# print(movies["year"])
movies_list = movies["genres"].apply(lambda x: x.split('|'))
# print(movies_list)
movies_drama = movies[(movies.genres == 'Drama')]
movies_drama1 = movies_drama[['genres','year']]
movies_drama1 = movies_drama1.groupby(['genres', 'year']).size().reset_index(name='count')


# bai 3 Hãy vẽ biểu đồ line chart mô tả tăng giảm của thể loại drama qua các năm
movies_drama1.plot.line( x = 'year', y='count')
tick_labels = tuple(movies_drama1['year'])
x_max = int(max(plt.xticks()[0]))  # int() to convert numpy.int32 => int
# manually set you xtick labels
plt.xticks(range(0, x_max + 1), tick_labels, rotation=45)
plt.show()
