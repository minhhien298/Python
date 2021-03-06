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
print(movies_drama1)

# bai 2 Hãy vẽ biểu đồ bar chart, mỗi cột ứng với thể loại phim
datacanve = pd.DataFrame.from_dict(counter_genres, orient='index').reset_index()
datacanve.plot( x = 'index',
        kind='bar',    # Plot a bar chart
        legend=False,    # Turn the Legend off
        width=0.75,      # Set bar width as 75% of space available
        figsize=(8,5.8),  # Set size of plot in inches
        color=[plt.cm.Paired(np.arange(len(datacanve)))])
plt.show()

