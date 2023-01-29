import pandas as pd

df1 = pd.read_csv("top_1000.csv")
df2 = pd.read_csv("mpst.csv")

df1 = df1.drop(['Metascore'], axis=1)

# titles list
def gen_titles_list():
    titles_list = []
    for i in range(1000):
        title = df1.loc[i,"Title"].lstrip(" .0123456789")[:-7]
        titles_list.append(title)
    return titles_list

# years list
def gen_years_list():
    years_list = []
    for i in range(1000):
        year = df1.loc[i,"Title"][-5:][:-1]
        years_list.append(year)
    return years_list

# durations list
def gen_durations_list():
    durations_list = []
    for i in range(1000):
        duration = df1.loc[i,"Duration"][:-4]
        durations_list.append(duration)
    return durations_list

# genres list
def gen_genres_list():
    genres_list = []
    for i in range(1000):
        genres = df1.loc[i,"Genre"]
        genres_list.append(genres.lower())
    for i in range(1000):
        if 'film-noir' in genres_list[i]:
            genres_list[i] = genres_list[i].replace('film-noir','').strip(" ,")
    return genres_list

genres_list = gen_genres_list()

def gen_unique_genres():
    unique_genres = []
    for i in range(1000):
        current_genres_tags = genres_list[i].split(',')
        for j in current_genres_tags:
            if j.strip() not in unique_genres:
                unique_genres.append(j.strip())
    unique_genres.sort()
    return unique_genres

# tags list
titles_list = gen_titles_list()

def gen_tags_list():
    tags_list = []
    for i in titles_list:
        tags = df2.loc[df2["title"] == i]["tags"].tolist()
        try:
            tags = tags[0].strip('\'')
        except:
            tags = ' '
        tags_list.append(tags)
    return tags_list

tags_list = gen_tags_list()

def gen_unique_tags():
    unique_tags = []
    for i in range(1000):
        if tags_list[i] == '':
            continue
        current_unique_tags = tags_list[i].split(',')
        for j in current_unique_tags:
            if j.strip() not in unique_tags:
                unique_tags.append(j.strip())
    unique_tags.sort()
    return unique_tags

# descriptions list
def gen_descriptions_list():
    descriptions_list = []
    for i in range(1000):
        description = df1.loc[i,"Description"]
        descriptions_list.append(description)
    return descriptions_list

# certificates list
def gen_certificates_list():
    certificates_list = []
    for i in range(1000):
        certificate = df1.loc[i,"Certificate"]
        certificates_list.append(certificate)
    for i in range(1000):
        if str(certificates_list[i]) in ['Approved','Not Rated','Passed','TV-MA','nan']:
            certificates_list[i] = 'R'
        elif certificates_list[i] in ['TV-PG','GP']:
            certificates_list[i] = 'PG'
        elif certificates_list[i] == 'TV-14':
            certificates_list[i] = 'PG-13'
    return certificates_list

# directors list
def gen_directors_list():
    directors_list = []
    for i in range(1000):
        bar = df1.loc[i,"Cast"].rfind('|')
        if df1.loc[i,"Cast"][8] == 's':
            director = df1.loc[i,"Cast"][11:bar-1]
        else:
            director = df1.loc[i,"Cast"][10:bar-1]
        directors_list.append(director)
    return directors_list

# actors list
def gen_actors_list():
    actors_list = []
    for i in range(1000):
        bar = df1.loc[i,"Cast"].rfind('|')
        actors = df1.loc[i,"Cast"][bar+9:]
        actors_list.append(actors)
    return actors_list

# create dataframe
df3 = pd.DataFrame({'Titles': gen_titles_list(),'Year': gen_years_list(),'Duration': gen_durations_list(),'Genre(s)': gen_genres_list(),'Tag(s)': gen_tags_list(),'Synopsis': gen_descriptions_list(),'Age Rating': gen_certificates_list(),'Director(s)': gen_directors_list(),'Star(s)': gen_actors_list()})

df3.to_csv('movie_data.csv')