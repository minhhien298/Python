import pandas as pd

movies = pd.read_csv("movies.csv")
movies2 = pd.DataFrame()
pd.options.mode.chained_assignment = None

genres_list = movies["genres"].apply(lambda x: x.split('|'))
flat_list = [item for sublist in genres_list for item in sublist]
drop_dups  = pd.Series(flat_list).drop_duplicates().tolist()
print(drop_dups)

movies2["id"] = movies["movieId"]
movies2["film"] = movies["title"].apply(lambda x: x.replace(x[-6:], '').split('|'))
movies2["year"] = pd.DataFrame(movies["title"].apply(lambda x: x[-6:-2] if x.endswith(" ")else x[-5:-1]))
movies2["genres"] = movies["genres"].apply(lambda x: x.split('|'))
print(movies2["genres"] )

for index,row in movies2.iterrows():
    for a in drop_dups:
       if a in  row["genres"]:
          movies2.loc[index,a] = 1
       else:
          movies2.loc[index,a] = 0

print(movies2["Action"])
# print(movies2)
print(movies2["Action"].corr(movies2["Adventure"]))

