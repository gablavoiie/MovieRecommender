from imdb import Cinemagoer
ia = Cinemagoer()

def takeinput(moviedict):
    if moviedict["simiar_movies"] != "no":
        movies = moviedict["similar_movies"]
        movlist = movies.split(",")
        res = []
        vectors = []
        for mov in movlist:
            res.append(ia.search_movie(mov)[0]["title"])
        for movie in res:
            
            vectors.append([]) # TO DO check if movie in csv file, if so query csv filet to get vector for movie with that title
    
    if movie["genres"] != "no":
        genreforvector = genreencoding(moviedict["genres"]) 
        
    if movie["decade"] != "no":
        decadecode = decadecoder(moviedict["decade"].strip())
       
    if movie["maturity"] != "no":
        maturitycode = maturitycoder(moviedict["maturity"])
    if movie["length"] != "no":
        length = movie["length"].strip().lower()
        if movie["length"] == "long" or movie["length"] == "longer":
            moviecode = 2
        if movie["length"] == "medium":
            moviecode = 1
        if movie["length"] == "short" or movie["length"] =="shorter":
            moviecode = 0
    #TODO if statement, check if they input anything for the "anything else?" and the how many movies do u want outputted, if not assign default

def lengthcoder(length):
    length.strip().lower() 
    ll = int(length)
    if length < 60:
        return 0
    elif 60 <= length <= 120:
        return 1
    elif length > 120:
        return 2
    return 500

def maturitycoder(maturity):
    maturity.lower().strip()
    if maturity == "g":
        return 0
    if maturity == "pg":
        return 1
    if maturity == "pg-13" or maturity =="pg13":
        return 2
    else:
        return 3
def decadecoder(year):
    
    year = year[:-1] 
   
    if year == "192":
        return 0
    elif year == "193":
        return 1
    elif year == "194":
        return 2
    elif year == "195":
        return 3
    elif year == "196":
        return 4
    elif year == "197":
        return 5
    elif year == "198":
        return 6
    elif year == "199":
        return 7
    elif year == "200":
        return 8
    elif year == "201":
        return 9
    elif year == "202":
        return 10
    else:
        return 100
        
            
def genreencoding(listofgenres):
    g = listofgenres.split(",")
    ppp = []
    for p in g:
        ppp.append(p.strip().lower())
    returnvector = [0]*20
    master = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
    for index, genre in enumerate(master):
        if genre.lower() in ppp:
            returnvector[index] = 1
    return returnvector

      

#def constructvector(decade, maturity, length, genre, tag):

dd = {"similar_movies": "lala", "genres": "Comedy , horror,adventure", "decade": "1956"}
takeinput(dd)