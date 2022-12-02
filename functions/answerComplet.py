import nltk
from .corpora.corpora import *

nltk.download('punkt')

def answerExtended(misspelledWord):


    def tokenizer(misspelledWord):
        if '-' in misspelledWord:
            return misspelledWord.split('-')
        elif ' ' in misspelledWord:
            return misspelledWord.split(' ')
        else:
            return misspelledWord.split()

    tokenWords = tokenizer(misspelledWord)

    def validation(misspelledWord):
        for prefix in allPrefixes:
            if misspelledWord.startswith(prefix):   
                ending = misspelledWord.replace(prefix, '')
                return [prefix, ending]

        
    validationWord = validation(misspelledWord)

    def normalization(tokenWords):

        if len(tokenWords) >= 2:
            return tokenWords
        elif len(tokenWords) < 2:
            return validationWord

    words = normalization(tokenWords)

    def hyphenating(words):

        if words[0] in wordsParts:
            for (p, e) in compoundWordsTuplas:
                if words[0] in p and words[1] in e.lower():
                    paragrafh = 'compound word'
                    return paragrafh


        elif words[0] in prefixCo:
            paragrafh = 'prefix co-'
            return paragrafh


        elif words[0] in prefixRe:
            paragrafh = 'prefix re-'
            return paragrafh


        elif words[0] in prefixDesIn:
            paragrafh = 'prefix des- in-'
            return paragrafh


        elif words[0] in prefixBem:
            paragrafh = 'prefix bem'
            return paragrafh


        elif words[0] in prefixNao:
            paragrafh = 'prefix não'
            return paragrafh


        elif words[0] in prefixSubSob:
            paragrafh = 'prefix sub- sob-'
            return paragrafh


        elif words[0] in prefixesSmall:
            paragrafh = 'prefix small'
            return paragrafh


        elif words[0] in pseudoprefixesNumber:
            paragrafh = 'prefix pseudon number'
            return paragrafh



        elif words[0] in prefixEr:
            paragrafh = 'prefix er'
            return paragrafh


        elif words[0] in prefixCircumPan:
            paragrafh = 'prefix circum- pan-'
            return paragrafh
            
        elif words[0] in prefixesHyphenated:
            paragrafh = 'prefix hyphenated'
            return paragrafh

        elif words[0] in prefixes or pseudoprefixes:
            paragrafh = 'prefix or pseudoprefix'
            return paragrafh


        elif words[0] in prefixSpecial:
            paragrafh = 'prefix special'
            return paragrafh



    correctWord=hyphenating(words)

    # if correctWord.startswith('mal') and correctWord[3] in vowels:
    #     paragrafh = 'prefix mal'
    #     return paragrafh
    
    return correctWord