# -*- coding: utf8 -*-

import math
import re
import pandas as pd
from nltk import bigrams
from nltk.util import ngrams
import nltk

def bigramCollection():
    import re
    import nltk
    import numpy as np
    import pandas as pd

    rawBook = open('data/Alice book.txt', 'r').read()
    book = re.sub("[^а-яА-Я]", " ", rawBook).lower()
    book = re.sub(" +", " ", book)
    print("Preproc book: ", book)

    bgs = nltk.bigrams(book)
    fdist = nltk.FreqDist(bgs)
    data = pd.DataFrame([k[0], k[1], v] for k, v in fdist.items()).rename(
        columns={0: 'Letter1', 1: 'Letter2', 2: 'Freq'})

    # for k,v in fdist.items():
    #     list= list.append ([k,v])
    data = data.sort_values(by=['Freq'], ascending=False)
    # for k,v in fdist.items():
    #     print (k,v)
    print(fdist.max())
    for i, row in data.iterrows():
        if row[0] != " " and row[1] != " ":
            print(row[0], row[1], row[2])

def replace(letter, shift):
    newLetter = ""

    if letter == " ":
        newLetter = " "
    elif letter in rusLow:
        newLetter = rusLow[(rusLow.index(letter) + shift % len(rusLow)) % len(rusLow)]

    elif letter in francLow:
        newLetter = francLow[(francLow.index(letter) + shift % len(francLow)) % len(francLow)]
    return newLetter

def distance(one, two):
    if one in rusLow:
        return rusLow.index(two) - rusLow.index(one)
    if one in francLow:
        return francLow.index(two) - francLow.index(one)
    return 0

def francRep(text):
    text = str(text)
    text = re.sub("^[ÀàÂâÆæ]", "a", text)
    text = re.sub("^[Çç]", "c", text)
    text = re.sub("^[ÉéÈèÊêËë]", "e", text)
    text = re.sub("^[ÎîÏï]", "i", text)
    text = re.sub("^[ÔôŒœ]", "o", text)
    text = re.sub("^[ÙùÛûÜü]", "u", text)
    text = re.sub("^[Ÿÿ]", "y", text)
    return text


rusLow = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
francLow = list('abcdefghijklmnopqrstuvwxyz')

rusFreqDict = {i : 0.0 for i in rusLow}
francFreqDict = {i : 0.0 for i in francLow}

rawBook = open('data/War and peace', 'r').read()
# print("Raw book: ", rawBook)
book = francRep(rawBook)
book = re.sub("[^а-яА-Яa-zA-Z]"," ", book).lower()
book = re.sub(" +", " ", book)
print("Preproc book: ", book)

newBook = ""
shift = 5
for letter in book:
    newBook += replace(letter, shift)
print("Encrypted book: ",newBook)

revBook = ""
for letter in newBook:
    revBook += replace(letter, -shift)
print("Reversed book: ",revBook)
print(book == revBook)

numRusLetters = 0
numfrancLetters = 0
numSpaces = 0

for letter in newBook:
    if letter in rusLow:
        rusFreqDict[letter] += 1
        numRusLetters += 1

    if letter in francLow:
        francFreqDict[letter] += 1
        numfrancLetters += 1

    if letter == " ": numSpaces +=1

for letter in rusFreqDict:
    rusFreqDict[letter] /= numRusLetters

for letter in francFreqDict:
    francFreqDict[letter] /= numfrancLetters

###
francMyFreq = pd.DataFrame([let,francFreqDict[let]] for let in francFreqDict).rename(columns={0 : 'Letter', 1: 'Freq'})
rusMyFreq = pd.DataFrame([let,rusFreqDict[let]] for let in rusFreqDict).rename(columns={0 : 'Letter', 1: 'Freq'})

###
# francWorldFreq = pd.read_csv('francFreq.csv')
francWorldFreq = pd.read_csv('data/FrenchFreq.csv')
# francWorldFreq['Freq'] = francWorldFreq['Freq'].str.replace('%', '').astype(float)*0.01
francWorldFreq['Freq'] = francWorldFreq['Freq']*0.01
rusWorldFreq = pd.read_csv('data/RusFreq.csv', encoding='windows-1251')
rusWorldFreq['Freq'] = rusWorldFreq['Freq'].str.replace('%', '').astype(float)*0.01

rusNewFreq = pd.concat([rusMyFreq.sort_values('Freq',ascending = False).reset_index(drop=True),
                        rusWorldFreq.sort_values('Freq',ascending = False).reset_index(drop=True)], axis=1, ignore_index=True)

francNewFreq = pd.concat([francMyFreq.sort_values('Freq',ascending = False).reset_index(drop=True),
                        francWorldFreq.sort_values('Freq',ascending = False).reset_index(drop=True)], axis=1, ignore_index=True)

##
tempFrame = pd.DataFrame(rusNewFreq[rusNewFreq[1] > rusNewFreq[1].mean()])
print(tempFrame)
predictedShift = 0
for index, row in tempFrame.iterrows():
    predictedShift += distance(row[0], row[2])
predictedShift = int(predictedShift / len(tempFrame))

###
predictBook = ''
for letter in newBook:
    predictBook += replace(letter, predictedShift)
print('Predict by one letter: ',predictBook)
print(book == predictBook)


tempFrame = pd.concat([rusNewFreq ,francNewFreq], axis=0)
# print(tempFrame)
replaceDict = {i[0] : i[2] for index, i in tempFrame.iterrows()}
replaceDict[' '] = ' '
print(replaceDict)
predictBook2 = ''
for letter in newBook:
    predictBook2 += replaceDict[letter]

print("Predict by all letters: ", predictBook2)

err = 0
for i in range(len(newBook)):
    if newBook[i] != predictBook2[i]: err += 1

print(1-(err)/len(newBook), len(newBook) == len(predictBook2))
print('\n')
print('Decrypting by bigrams')
bigramCollection()

preBook = re.sub("х[^а-я]", "", newBook)
bgs = bigrams(preBook)
fdist = nltk.FreqDist(bgs)
data = pd.DataFrame([k[0], k[1],v] for k,v in fdist.items()).rename(columns={0 : 'Letter1', 1: 'Letter2', 2: 'Freq'})
data = data.sort_values(by=['Freq'], ascending=False)

for i, row in data.iterrows():
    if row[0] != " " and row[1] != " ":
        print("1: ",row[0],row[0] in rusLow, distance(row[0], "т"))
        print("2: ",row[1],row[1] in rusLow, distance(row[1], "о"))
        if distance(row[0], "т") == distance(row[1], "о"):
            predictedShift = distance(row[1], "о")
            break

predictBook = ''
for letter in newBook:
    predictBook += replace(letter, predictedShift)
print('Predict by one bigram: ',predictBook)
print(book == predictBook)


