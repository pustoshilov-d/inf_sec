# -*- coding: utf8 -*-
import re
import nltk
import numpy as np
import pandas as pd


rawBook = open('data/Alice book.txt', 'r').read()
book = re.sub("[^а-яА-Я]"," ", rawBook).lower()
book = re.sub(" +", " ", book)
print("Preproc book: ", book)

bgs = nltk.bigrams(book)
fdist = nltk.FreqDist(bgs)
data = pd.DataFrame([k[0], k[1],v] for k,v in fdist.items()).rename(columns={0 : 'Letter1', 1: 'Letter2', 2: 'Freq'})

# for k,v in fdist.items():
#     list= list.append ([k,v])
data = data.sort_values(by=['Freq'], ascending=False)
# for k,v in fdist.items():
#     print (k,v)
print(fdist.max())
for i, row in data.iterrows():
    if row[0] != " " and row[1] != " ":
        print(row[0], row[1], row[2])
