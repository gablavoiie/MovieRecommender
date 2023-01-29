import pandas
import numpy as np

# this script is run on a constrained frame

def calculate_similarity(a, b):
      return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

df = pandas.read_csv("movie_data.csv")
def strtovector(uservector):
    lista = []

    lista.append(int(uservector[1]))
   
    lista.append(int(uservector[4]))
   
    listagenre = []
    for i in range(8,68,3):
        listagenre.append(int(uservector[i]))
    
    listatag = []
    for i in range(70,277,3):
        if int(uservector[i]) == 0:
            listatag.append(int(uservector[i]))
        else:
            listatag.append(15)
    lista.append(listagenre)
    lista.append(listatag)
  
    return(lista)

def calculate_score(movievector,uservector):
    v = strtovector(movievector)
    
    va = []
    vb = []
    va.append(v[0])
    va.append(v[1])
    vb.append(uservector[0])
    vb.append(uservector[1])
    for n in v[2]:
        va.append(n)
    for m in v[3]:
        va.append(m)
    for p in uservector[2]:
        vb.append(p)
    for q in uservector[3]:
        vb.append(q)
    
    return(calculate_similarity(va,vb))