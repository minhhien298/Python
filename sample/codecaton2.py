import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

movies = pd.read_csv("movies.csv")
pd.options.mode.chained_assignment = None
genres_list = movies["genres"].apply(lambda x: x.split('|'))
flat_list = [item for sublist in genres_list for item in sublist]
counter_genres = Counter(flat_list)


# bai 2 Hãy vẽ biểu đồ bar chart, mỗi cột ứng với thể loại phim
datacanve = pd.DataFrame.from_dict(counter_genres, orient='index').reset_index()
print(datacanve)
datacanve.plot( x = 'index',
        kind='bar',    # Plot a bar chart
        legend=False,    # Turn the Legend off
        width=0.75,      # Set bar width as 75% of space available
        figsize=(8,5.8),  # Set size of plot in inches
        color=[plt.cm.Paired(np.arange(len(datacanve)))])
plt.show()

