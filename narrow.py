from imdb import Cinemagoer
import pandas as pd

ia = Cinemagoer()
df3 = pd.read_csv("movie_data.csv")

def narrow(index,maturity,director_star):    
    maturity = maturity.lower().strip()
    director_star = director_star.lower().strip()
    if df3.iloc[index,8].lower().strip() != maturity and maturity != "no":
  
        return False

    director_star_list = director_star.split(', ')
 
    if director_star_list != [''] and director_star_list != ['no']:
        for person in director_star_list:
            if str(ia.search_person(person)[0]) not in (df3.iloc[index,9] + ', ' + df3.iloc[index,10]).split(', '):
               return False
    return True

  