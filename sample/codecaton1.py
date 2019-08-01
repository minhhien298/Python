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
print(counter_genres)