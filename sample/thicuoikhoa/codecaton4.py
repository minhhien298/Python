import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv("movies.csv")
pd.options.mode.chained_assignment = None
genres_list = movies["genres"].apply(lambda x: x.split('|'))
flat_list = [item for sublist in genres_list for item in sublist]

# bai 1 Hãy liệt kê tất cả các thể loại phim theo tần suất xuất hiện
counter_genres = Counter(flat_list)

#https://stackoverflow.com/questions/29233283/plotting-multiple-lines-with-pandas-dataframe
movies["year"] = movies["title"].apply(lambda x: x[-6:-2] if x.endswith(" ")  else x[-5:-1] )#if isinstance(x[-6:-2], int) is True else "unknown")
movies_list = movies["genres"].apply(lambda x: x.split('|'))
movies_drama = movies[(movies.genres == 'Drama')|(movies.genres == 'Comedy')|(movies.genres == 'Thriller')]
movies_drama1 = movies_drama[['genres','year']]
movies_drama1 = movies_drama1.groupby(['genres', 'year']).size().reset_index(name='count')

# bai 4 Hãy vẽ biểu đô line chart mô tả tăng giảm của 3 thể loại phim phổ biến nhất qua các năm
# https://stackoverflow.com/questions/46717359/pandas-plot-multiple-category-lines
fig, ax = plt.subplots()
for label, grp in movies_drama1.groupby('genres'):
    grp.plot(x = 'year', y = 'count',ax = ax, label = label)
plt.show()



