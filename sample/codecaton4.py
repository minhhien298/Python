
from collections import Counter
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv("movies.csv")
pd.options.mode.chained_assignment = None
genres_list = movies["genres"].apply(lambda x: x.split('|'))
flat_list = [item for sublist in genres_list for item in sublist]
counter_genres = Counter(flat_list)
datacanve = pd.DataFrame.from_dict(counter_genres, orient='index').reset_index()
# print(datacanve['index'].iloc[0])


# bai 1 Hãy liệt kê tất cả các thể loại phim theo tần suất xuất hiện
counter_genres = Counter(flat_list)

#https://stackoverflow.com/questions/29233283/plotting-multiple-lines-with-pandas-dataframe
movies["year"] = movies["title"].apply(lambda x: x[-6:-2] if x.endswith(" ")  else x[-5:-1] )#if isinstance(x[-6:-2], int) is True else "unknown")
movies_list = movies["genres"].apply(lambda x: x.split('|'))
movies_drama = movies[(movies.genres == datacanve['index'].iloc[0])|(movies.genres == datacanve['index'].iloc[1])|(movies.genres == datacanve['index'].iloc[2])]
movies_drama1 = movies_drama[['genres','year']]
movies_drama1 = movies_drama1.groupby(['genres', 'year']).size().reset_index(name='count')
# print(movies_drama1)

# bai 4 Hãy vẽ biểu đô line chart mô tả tăng giảm của 3 thể loại phim phổ biến nhất qua các năm
# https://stackoverflow.com/questions/46717359/pandas-plot-multiple-category-lines

print(movies_drama1)
movies_drama1["year"] = pd.to_datetime(movies_drama1["year"])
fig, ax = plt.subplots()
for label, grp in movies_drama1.groupby('genres'):
    grp.plot(x = 'year', y = 'count',ax = ax, label = label)
plt.show()
'''


fig, ax = plt.subplots()

for key, grp in movies_drama1.groupby(['genres']):
    ax = grp.plot(ax=ax, kind='line', x='year', y='count', c=key, label=key)

plt.legend(loc='best')
plt.show()

'''
'''
# https://stackoverflow.com/questions/46870672/multiple-lines-on-line-plot-time-series-with-matplotlib-or-plot-ly-on-python

print(movies_drama1)
movies_drama1["year"] = pd.to_datetime(movies_drama1["year"])
movies_drama1.pivot(index="year", columns="genres", values="count").plot()

plt.show()


'''
