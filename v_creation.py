import pandas as pd
from coding import *

df3 = pd.read_csv("movie_data.csv")

# create individual vector for given movie
def create_vector(n):
    year = decade_coder(str(df3.iloc[n,2].tolist()))
    length = length_coder(df3.iloc[n,3].tolist())
    genres = genre_encoding(df3.iloc[n,4])
    tags = tag_encoding(df3.iloc[n,5])
    vector = [year,length,genres,tags]
    return vector

# generate list of vectors for all movies
def vector_list():
    vectors = []
    for i in range(1000):
        vectors.append(create_vector(i))
    return vectors

vectors = vector_list()

# add vectors to dataframe
df3['Vector'] = vectors
df3.to_csv('movie_data.csv')