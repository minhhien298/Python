import pandas as pd
df = pd.read_csv('movies.csv', encoding="utf8")
if df["title"].apply(lambda x:(x[-5:-1])).any() =="1995":
      print(df['genres'].value_counts()) # .idxmax()



