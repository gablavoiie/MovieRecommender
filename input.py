from imdb import Cinemagoer

ia = Cinemagoer()

def take_input(moviedict):
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



#def constructvector(decade, maturity, length, genre, tag):

dd = {"similar_movies": "lala", "genres": "Comedy , horror,adventure", "decade": "1956"}
take_input(dd)