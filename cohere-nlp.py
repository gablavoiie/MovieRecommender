import cohere
import numpy as np
import re
import pandas as pd
from cohere.classify import Example
import csv

co = cohere.Client('oCNTguHRKMkKQ6wiXNFmDrb8ZeHVYbnDbsXcq5W1')

examples=[   #5-50 examples
  Example("The order came 5 days early", "positive"), 
  Example("The item exceeded my expectations", "positive"), 
  Example("I ordered more for my friends", "positive"), 
  Example("I would buy this again", "positive"), 
  Example("I would recommend this to others", "positive"), 
  Example("The package was damaged", "negative"), 
  Example("The order is 5 days late", "negative"), 
  Example("The order was incorrect", "negative"), 
  Example("I want to return my item", "negative"), 
  Example("The item\'s material feels low quality", "negative"), 
  Example("The product was okay", "neutral"), 
  Example("I received five items in total", "neutral"), 
  Example("I bought it from the website", "neutral"), 
  Example("I used the product this morning", "neutral"), 
  Example("The product arrived yesterday", "neutral"),
]


def get_sentiment(input):
  r = [input]
  response = co.classify(
  model='large',
  inputs=r,
  examples=examples,
  )
  return(response.classifications[0].prediction)

def get_similarity(input, movie):
  phrases = [input,movie]
  [r,x] = co.embed(phrases).embeddings
  def calculate_similarity(a, b):
      return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
  return calculate_similarity(r,x)



def clean_text(
  string: str, 
  punctuations=r'''!()-[]{};:'"\,<>./?@#$%^&*_~''',
  stop_words=['the', 'a', 'and', 'is', 'be', 'will']) -> str:
  """
  A method to clean text 
  """
  # Cleaning the urls
  string = re.sub(r'https?://\S+|www\.\S+', '', string)

  # Cleaning the html elements
  string = re.sub(r'<.*?>', '', string)

  # Removing the punctuations
  for x in string.lower(): 
      if x in punctuations: 
          string = string.replace(x, "") 

  # Converting the text to lower
  string = string.lower()

  # Removing stop words
  string = ' '.join([word for word in string.split() if word not in stop_words])

  # Cleaning the whitespaces
  string = re.sub(r'\s+', ' ', string).strip()

  return string



# data preprocessing
vectors = {}
df = pd.read_csv("mpst_full_data.csv")
for a in df.index:
  plot = df["plot_synopsis"][a]
  plot = clean_text(plot)
  tokenized = co.tokenize(plot)
  strr = ""
  
        
    
  embed = co.embed([strr]).embeddings
  embeds = tuple(embed)
  p = df["tags"][a]
  n = []
  for ii in p:
    n.append(ii.strip())
  pp = tuple(n)
  vectors["r"] = pp
      
for i in range(1):
      print(vectors)
    

