import pandas as pd

df1 = pd.read_csv("top_1000.csv")
df2 = pd.read_csv("mpst.csv")

print(df1.to_string())