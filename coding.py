def decade_coder(year):
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
    else:
        return 1000

'''
def maturity_coder(maturity):
    maturity.lower().strip()
    if maturity == "g":
        return 0
    elif maturity == "pg":
        return 1
    elif maturity == "pg-13" or maturity =="pg13":
        return 2
    elif maturity == "r":
        return 3
    else:
        return 1000
'''

def length_coder(length):
    length = int(length)
    if length < 60:
        return 0
    elif 60 <= length <= 120:
        return 1
    elif length > 120:
        return 2
    else:
        return 1000

def genre_encoding(str_of_genres):
    master = ['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'drama', 'family', 'fantasy', 'history', 'horror', 'music', 'musical', 'mystery', 'romance', 'sci-fi', 'sport', 'thriller', 'war', 'western']
    list_of_genres = str_of_genres.split(",")
    processed_list = []
    for i in list_of_genres:
        processed_list.append(i.strip().lower())
    genre_vector = [0]*len(master)
    for index, genre in enumerate(master):
        if genre in processed_list:
            genre_vector[index] = 1
    return genre_vector

def tag_encoding(str_of_tags):
    master = ['absurd', 'action', 'adult comedy', 'allegory', 'alternate history', 'alternate reality', 'anti war', 'atmospheric', 'autobiographical', 'avant garde', 'blaxploitation', 'bleak', 'boring', 'brainwashing', 'claustrophobic', 'clever', 'comedy', 'comic', 'cruelty', 'cult', 'cute', 'dark', 'depressing', 'dramatic', 'entertaining', 'fantasy', 'feel-good', 'flashback', 'good versus evil', 'gothic', 'haunting', 'historical', 'historical fiction', 'home movie', 'horror', 'humor', 'insanity', 'inspiring', 'intrigue', 'magical realism', 'melodrama', 'murder', 'mystery', 'neo noir', 'non fiction', 'paranormal', 'philosophical', 'plot twist', 'pornographic', 'prank', 'psychedelic', 'psychological', 'queer', 'realism', 'revenge', 'romantic', 'sadist', 'satire', 'sci-fi', 'sentimental', 'storytelling', 'stupid', 'suicidal', 'suspenseful', 'thought-provoking', 'tragedy', 'violence', 'western', 'whimsical']
    list_of_tags = str_of_tags.split(",")
    processed_list = []
    for i in list_of_tags:
        processed_list.append(i.strip().lower())
    tag_vector = [0]*len(master)
    for index, tag in enumerate(master):
        if tag in processed_list:
            tag_vector[index] = 1
    return tag_vector