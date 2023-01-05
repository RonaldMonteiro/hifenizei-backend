import nltk
from .corpora.corpora import *

nltk.download('punkt')

def answer(misspelledWord):


    def tokenizer(misspelledWord):
        if '-' in misspelledWord:
            return misspelledWord.split('-')
        elif ' ' in misspelledWord:
            return misspelledWord.split(' ')
        else:
            return misspelledWord.split()

    tokenWords = tokenizer(misspelledWord)
    print(tokenWords)
    def validation(misspelledWord):
            for prefix in all_words:
                if misspelledWord.startswith(prefix):   
                    ending = misspelledWord.replace(prefix, '')
                    return [prefix, ending]
            else:
                return 'error'
        
    validationWord = validation(misspelledWord)
    print(validationWord)

    def normalization(misspelledWord):
        if validationWord == 'error':
            return 'error'
        elif len(tokenWords) == 1:
            return validationWord
        elif len(tokenWords) >= 2:
            return tokenWords


    words = normalization(validationWord)
    print(words)

    def hyphenating(words):
        if misspelledWord == 'email' or misspelledWord == 'e mail' or misspelledWord == 'e-mail':
            
            paragraf = 'Algumas palavras compostas, como "e-mail", são separadas convencionalmente por hífen para manter a noção de composição semântica e sintagmática, sem haver uma regra que rege necessariamente o caso. Mas pode ser que a palavra represente um topônimo ou uma espécie de planta ou animal. Independente de seu enquadramento, sempre serão grafadas com hífen.'
            return paragraf
        else:
            pass

        for element in list_repet:
            if misspelledWord.startswith(element[0]):       
                text = element[0]+'-'+element[1]         
                paragraf = f'Algumas palavras compostas, como "{text}", são separadas convencionalmente por hífen para manter a noção de composição semântica e sintagmática, sem haver uma regra que rege necessariamente o caso. Mas pode ser que a palavra represente um topônimo ou uma espécie de planta ou animal. Independente de seu enquadramento, sempre serão grafadas com hífen.'
                return paragraf
            else:
                pass

        if len(tokenWords) ==3:
            for l in list_phrase:
                if tokenWords[0] == l[0] and tokenWords[1] == l[1] and tokenWords[2] == l[2]:
                    text = l[0]+'-'+l[1]+'-'+l[2]         
                    paragraf = f'Algumas palavras compostas, como "{text}", são separadas convencionalmente por hífen para manter a noção de composição semântica e sintagmática, sem haver uma regra que rege necessariamente o caso. Mas pode ser que a palavra represente um topônimo ou uma espécie de planta ou animal. Independente de seu enquadramento, sempre serão grafadas com hífen.'
                    return paragraf
        else:
            pass


        for prefix in list_exception:
            if misspelledWord.startswith(prefix[0]):
                ending = misspelledWord.replace(prefix[0], '')
                if ending[1:] == prefix[1]:
                    text = prefix[0]+'-'+prefix[1]         
                    paragraf = f'Algumas palavras compostas, como "{text}", são separadas convencionalmente por hífen para manter a noção de composição semântica e sintagmática, sem haver uma regra que rege necessariamente o caso. Mas pode ser que a palavra represente um topônimo ou uma espécie de planta ou animal. Independente de seu enquadramento, sempre serão grafadas com hífen.'
                    return paragraf
                else:
                    
                    return 'not'
            else:
                pass
                    

        if words == 'error':
            return 'error'
        elif '-' in words:
            paragraf = f'Algumas palavras compostas, como "{validationWord}", são separadas convencionalmente por hífen para manter a noção de composição semântica e sintagmática, sem haver uma regra que rege necessariamente o caso. Mas pode ser que a palavra represente um topônimo ou uma espécie de planta ou animal. Independente de seu enquadramento, sempre serão grafadas com hífen.'
            return paragraf
        elif words[0] in words_parts:
            for (p, e) in compound_words_tuplas:
                if words[0] in p and words[1] in e.lower():
                    text = words[0] +'-'+words[1]
                    paragraf = f'Algumas palavras compostas, como "{text}", são separadas convencionalmente por hífen para manter a noção de composição semântica e sintagmática, sem haver uma regra que rege necessariamente o caso. Mas pode ser que a palavra represente um topônimo ou uma espécie de planta ou animal. Independente de seu enquadramento, sempre serão grafadas com hífen.'
                    return paragraf
            else:
                return 'error'      
        
        elif words[0] in prefix_co:
            paragraf = 'Palavras iniciadas por prefixo “co” nunca levarão hífen, mesmo nos casos em que o segundo elemento começar com “h” ou “o”. No entanto, quando o segundo elemento começar por “r” ou “s”, a palavra terá essas consoantes duplicadas. Em todas as situações as palavras serão grafadas juntas.'
            return paragraf


        elif words[0] in prefix_re:
            paragraf = 'Palavras iniciadas por prefixo “re” nunca levarão hífen. Em todas as situações as palavras serão grafadas juntas.'
            return paragraf
            
        elif words[0] in prefixes_des_in:
            paragraf = f'Palavras iniciadas por prefixo “{words[0]}” nunca levarão hífen. Em todas as situações as palavras serão grafadas juntas.'
            return paragraf
            
        elif words[0] in prefix_bem:
            paragraf = 'Palavras compostas iniciadas pelo prefixo “bem” sempre levarão hífen.  Há algumas exceções como as palavras benfeitoria, benfeito, benfeitor.'
            return paragraf
            
        elif words[0] in prefix_nao:
            paragraf = 'Palavras que contenham o “não” como prefixo nunca levarão hífen. Em todas as situações as palavras serão grafadas separadas.'
            return paragraf

        elif words[0] in prefixes_sub_sob:
            paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” sempre levarão hífen quando o segundo elemento começar com “b” ou “r”. Mas se começar com “h”, poderá a palavra tanto ser hifenizada como grafada junta e com a omissão da letra “h”. Nas demais situações as palavras serão grafadas juntas. '
            return paragraf
                
        elif words[0] in prefixes_small:
            paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” sempre levarão hífen quando o segundo elemento iniciar com “r”. Nas demais situações as palavras serão grafadas juntas. '
            return paragraf
            
        elif words[0] in pseudoprefixes_number:
            paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” nunca levarão hífen. Em todas as situações as palavras serão grafadas juntas. '
            return paragraf
            
        elif words[0] in prefixes_er:
            paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” sempre levarão hífen quando o segundo elemento iniciar com “h” ou “r”.  Nas demais situações as palavras serão grafadas juntas. '
            return paragraf
                    
        elif words[0] in prefixes_circum_pan:
            paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” sempre levarão hífen quando o segundo elemento iniciar com “h”, “m”, “n” ou vogal. Nas demais situações as palavras serão grafadas juntas. '
            return paragraf
            
        elif words[0] in prefixes_hyphenated:
            paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” sempre levarão hífen. Em nenhuma situação as palavras serão grafadas juntas ou separadas.  '
            return paragraf

        elif words[0] in prefixes_default or pseudoprefixes:
            if words[0][-1] == words[1][0]:
                paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” sempre levarão hífen quando o segundo elemento iniciar com a mesma vogal que termina o primeiro. Nos casos em que as letras forem diferentes, as palavras serão grafadas juntas.  '
                return paragraf
            elif words[1][0] == 'h':
                paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” sempre levarão hífen quando o segundo elemento iniciar com a consoante “h”. '
                return paragraf
            elif words[0][-1] in vowels and words[1][0] == 'r':
                paragraf = f'Palavras compostas iniciadas pelo prefixo "{words[0]}" nunca levarão hífen quando o segundo elemento iniciar com “r” ou “s”. Nesses casos as palavras serão aglutinadas, sendo grafadas com essas consoantes duplicadas.  '
                return paragraf
            elif words[0][-1] in vowels and words[1][0] == 's':
                paragraf = f'Palavras compostas iniciadas pelo prefixo "{words[0]}" nunca levarão hífen quando o segundo elemento iniciar com “r” ou “s”. Nesses casos as palavras serão aglutinadas, sendo grafadas com essas consoantes duplicadas. '
                return paragraf
            elif words[0][-1] in vowels and words[1][0] in vowels:
                if words[0][-1] != words[1][0]:
                    paragraf = f'Palavras compostas iniciadas pelo prefixo “{words[0]}” nunca levarão hífen quando o segundo elemento iniciar com uma vogal diferente da vogal que termina o primeiro. Nos casos em que as letras forem iguais, as palavras serão grafadas com hífen.'
                    return paragraf
            elif words[0] in prefix_mal:
                paragraf = f'Palavras compostas iniciadas pelo advérbio “{words[0]}” sempre levarão hífen quando o segundo elemento iniciar por “h”, “l” ou vogal. Nas demais situações as palavras serão grafadas juntas. '
                return paragraf        
            else:
                return 'ERROR'

        # elif words[0] in prefixSpecial:
        #     paragraf = f'Palavras compostas iniciadas pelo advérbio “{words[0]}” sempre levarão hífen quando o segundo elemento iniciar por “h”, “l” ou vogal. Nas demais situações as palavras serão grafadas juntas. '
        #     return paragraf

        # else:
        #     return 'error'

    answerText=hyphenating(words)

    return answerText

x = answer('malestar')
print(x)
