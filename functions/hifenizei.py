import nltk
from .corpora.corpora import *

nltk.download('punkt')


def hifenizei(misspelledWord):


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
                    
            else:
                return 'error'
           
        
    validationWord = validation(misspelledWord)
    print(validationWord)


    def validationSecond(validationWords):
        if validationWord != 'error':
            for pala in prefixesSeconds:
                if misspelledWord.endswith(pala):
                    return validationWord
                
                    
            else:
                return 'error'
        else:
            return 'error'

    validationWordSecond = validationSecond(validationWord)
    print(validationWordSecond)

    # def validationTree(validationWord):
    #     if validationWord == 'error':
    #         for pala in WordsSeconds:
    #             if misspelledWord.endswith(pala):
    #                 return validationWord
                    
    #         else:
    #             return 'error'
    #     else:
    #         return validationWordSecond


    # validationWordTree = validationTree(validationWordSecond)
    # print(validationWordTree)

    def normalization(misspelledWord):
        if validationWordSecond == 'error':
            return 'error'
        elif len(tokenWords) == 1:
            return validationWordSecond
        elif len(tokenWords) >= 2:
            return tokenWords

    words = normalization(validationWordSecond)
    print(words)
    def hyphenating(words):
        if misspelledWord == 'email' or misspelledWord == 'e mail' or misspelledWord == 'e-mail':
            return 'e-mail'
        else:
            pass

        if misspelledWord == 'obra-prima' or misspelledWord == 'obra prima' or misspelledWord == 'obraprima':
            return 'obra-prima'
        else:
            pass

        for element in listRepetNormalization:
            if misspelledWord.startswith(element[0]):
                return element[0] +'-'+ element[0]
            else:
                pass

        if len(tokenWords) ==3:
            for l in listPhraseNormalization:
                if tokenWords[0] == l[0] and tokenWords[1] == l[1] and tokenWords[2] == l[2]:
                    return l[0]+'-'+l[1]+'-'+l[2]
        else:
            pass


        for prefix in listExceptionNormalization:
            if misspelledWord.startswith(prefix[0]) and misspelledWord.endswith(prefix[1]):
                ending = misspelledWord.replace(prefix[0], '')
                print(prefix[1])
                if ending == prefix[1]:
                    return prefix[0] + '-' + ending
                else:
                    return 'not'
            else:
                pass
                    

        if words == 'error':
            return 'error'
        elif '-' in words:
            return validationWord
        elif words[0] in wordsParts:
            for (p, e) in compoundWordsTuplas:
                if words[0] in p and words[1] in e.lower():
                    return words[0] + '-' + words[1]
            else:
                return 'error'      
        
        elif words[0] in prefixCo:
            if words[1][0] == 'r' and words[1][1] == 'r':
                correctWord = words[0] + words[1]
                return correctWord 
            elif words[1][0] =='r':
                correctWord = words[0] +'r'+ words[1]
                return correctWord
            elif words[1][0] == 's' and words[1][1] == 's':
                correctWord = words[0] + words[1]
                return correctWord 
            elif words[1][0] == 's':
                correctWord = words[0] + 's' + words[1]
                return correctWord
            elif words[1][0] == 'h':
                correctWord = words[0] + words[1][1:]
                return correctWord
            else:
                correctWord = words[0] + words[1]
                return correctWord

        elif words[0] in prefixRe:
            correctWord = words[0] + words[1]
            return correctWord
            
        elif words[0] in prefixDesIn:
            if words[1][0] == 'h':
                correctWord = words[0] + words[1][1:]
                return correctWord
            else:
                correctWord = words[0] + words[1]
                return correctWord
            
        elif words[0] in prefixBem:
            correctWord = words[0] + '-' + words[1]
            exceptionWord = words[0][:2] + 'n' + words[1]
            if words[1] == 'feitor':
                return exceptionWord
            elif words[1] == 'feito':
                return exceptionWord
            else:
                return correctWord
            
        elif words[0] in prefixNao:
            correctWord = words[0] + ' ' + words[1]
            return correctWord

        elif words[0] in prefixSubSob:
            if words[1][0] == 'b':
                correctWord= words[0]+'-'+words[1]
                return correctWord
            elif words[1][0] == 'r':
                correctWord= words[0]+'-'+ words[1]
                return correctWord
            elif 'human' in words[1]:
                correctWord = words[0] + words[1][1:]
                return correctWord
            elif words[1][0] == 'h':
                correctWord= words[0]+'-'+words[1]
                return correctWord
            else:
                correctWord=words[0]+words[1]
                return correctWord
                
        elif words[0] in prefixesSmall:
            if words[1][0] == 'r':
                correctWord=words[0] + '-' + words[1]
                return correctWord
            else:
                correctWord=words[0] + words[1]
                return correctWord
            
        elif words[0] in pseudoprefixesNumber:
            correctWord=words[0]+words[1]
            return correctWord
            
        elif words[0] in prefixEr:
            if words[1][0] == 'h':
                correctWord=words[0]+'-'+words[1]
                return correctWord
            elif words[1][0] == 'r':
                correctWord=words[0]+'-'+words[1]
                return correctWord
            else:
                correctWord=words[0]+words[1]
                return correctWord
                    
        elif words[0] in prefixCircumPan:
            if words[1][0] == 'h':
                correctWord=words[0]+'-'+words[1]
                return correctWord
            elif words[1][0] == 'n':
                correctWord=words[0]+'-'+words[1]
                return correctWord
            elif words[1][0] == 'm':
                correctWord=words[0]+'-'+words[1]
                return correctWord
            else:
                correctWord=words[0]+words[1]
                return correctWord
            
        elif words[0] in prefixesHyphenated:
            correctWord=words[0] + '-' + words[1]
            return correctWord

        elif words[0] in prefixes or pseudoprefixes:
            if words[0][-1] == words[1][0]:
                correctWord =  words[0] + '-' + words[1]
                return correctWord
            elif words[1][0] == 'h':
                correctWord=words[0] + '-' + words[1]
                return correctWord
            
            elif words[0][-1] in vowels and words[1][0] == 'r' and words[1][1] == 'r':
                # if words[1][0] == 'r' and words[1][1] == 'r':
                correctWord = words[0] + words[1]
                return correctWord 

            elif words[0][-1] in vowels and words[1][0] == 'r':
                correctWord=words[0] + 'r' + words[1]
                return correctWord


            elif words[0][-1] in vowels and words[1][0] == 's' and words[1][1] == 's':
                # if words[1][0] == 's' and words[1][1] == 's':
                correctWord = words[0] + words[1]
                return correctWord   


            elif words[0][-1] in vowels and words[1][0] == 's':
                correctWord=words[0] + 's' + words[1]
                return correctWord


            elif words[0][-1] in vowels and words[1][0] in vowels:
                if words[0][-1] != words[1][0]:
                    correctWord=words[0]+words[1]
                    return correctWord
            else:
                correctWord = words[0] + words[1]
                return correctWord

        elif words[0] in prefixSpecial:
            if words[1][0] in vowels:
                correctWord=words[0] + '-' + words[1]
                return correctWord
            elif words[1][0] in h_and_l:
                correctWord=words[0]+'-'+words[1]
                return correctWord
            else:
                correctWord=words[0] + words[1]
                return correctWord

        elif words == 'error':
            return 'error'

    correctWord=hyphenating(words)

    if correctWord.startswith('mal') and correctWord[3] in vowels:
        l = correctWord.replace('mal', '')
        answer = 'mal-'+l
    else:
        answer = correctWord
    


    return answer

# x = hifenizei('micro jkajsajs')
# print(x)


