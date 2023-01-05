import nltk
from .corpora.corpora import *

# nltk.download('punkt')
nltk.download('punkt')


def hifenizei(entry):

    def tokenizer(entry):
        def unstik(word):
            for prefix in list_phrase:
                if word.startswith(prefix[0]) and word.endswith(prefix[2]):
                    data = prefix
                    return data
            else:
                pass

            repet = sorted(list_repet, key = len, reverse = True)

            for tupla in repet:
                for prefix in tupla:
                    if word.startswith(prefix): 
                        ending = word.replace(prefix, '')
                        data = [prefix, prefix]
                        return data
            else:
                pass

            compound = sorted(words_parts, key = len, reverse = True)

            for prefix in compound:
                if word.startswith(prefix): 
                    ending = word.replace(prefix, '')
                    data = [prefix, ending]
                    return data
            else:
                pass

            prefixes = sorted(all_prefixes, key = len, reverse = True)

            for prefix in prefixes:
                if word.startswith(prefix): 
                    ending = word.replace(prefix, '')
                    data = [prefix, ending]
                    return data
            else:
                data = 'error unstick'
                return data

        if '-' in entry:
            data = entry.split('-')
        elif ' ' in entry: 

            data = entry.split(' ')
        else:
            data = unstik(entry)

        return data

    tokens = tokenizer(entry)
    print(tokens)
    def validation(tokens):
        def compound(word, ending):
            for tupla in list_repet:
                if word == tupla[0] and ending == tupla[1].lower():
                    data = [word, ending]
                    return data
            else:
                pass

            for tupla in compound_words_tuplas:
                if word == tupla[0] and ending == tupla[1].lower():
                    data = [word, ending]
                    return data
            else:
                pass
            
            for tupla in list_exception:
                if word == tupla[0] and ending == tupla[1]:
                    data = [word, ending]
                    return data
            else:
                pass
            
            # for prefix in all_prefixes:
            #     if word == prefix and ending in all_terms:
            #         data = [word, ending]
            #         return data
            #     else:
            #         return '?'
            if word in all_prefixes and ending in all_terms:
                    data = [word, ending]
                    return data
            elif word in all_prefixes and ending[1:] in all_terms:
                    data = [word, ending[1:]]
                    return data            
            else:
                return 'error'
            # else:
            #     data = 'error validation compound'
            #     return data

        def phrase(word, preposition, ending):
            for prefix in list_phrase:
                if word == prefix[0] and preposition == prefix[1] and ending == prefix[2]:
                    data = [word, preposition, ending]
                    return data
                else:
                    data = 'error'
        
        if tokens != 'error unstick':
            if len(tokens) == 3:
                data = phrase(tokens[0], tokens[1], tokens[2])
                return data
            elif len(tokens) == 2:
                data = compound(tokens[0], tokens[1])
                return data
            else:
                data = 'error'
                return data
        else:
            data_error = 'error'
            return data_error

    list_words = validation(tokens)
    print(list_words)

    def hyphenating(words):
        def compound(words):
            if len(words) == 3:
                for prefix in list_phrase:
                    if words[0] == prefix[0] and words[1] == prefix[1] and words[2] == prefix[2]:
                        data = words[0] + '-' + words[1] + '-' + words[2]
                        return data
                else:
                    pass
            elif len(words) == 2:
                for tupla in list_repet:
                    if words[0] == tupla[0] and words[1] == tupla[1]:
                        data = words[0] + '-' + words[1]
                        return data
                else:
                    pass

                for tupla in compound_words_tuplas:
                    if words[0] == tupla[0] and words[1] == tupla[1].lower():
                        data = words[0] + '-' + words[1]
                        return data
                else:
                    pass
            
                for tupla in list_exception:
                    if words[0] == tupla[0] and words[1] == tupla[1]:
                        data = words[0] + '-' + words[1]
                        return data
                else:
                    return 'prefixo'
            else:
                return 'error hyphenating'

        compound_hyphenating = compound(words)

        def prefixCo(prefix, ending):
            if ending[0] == 'r' and ending[1] == 'r':
                data = prefix + ending
                return data 
            elif ending[0] =='r':
                data = prefix + 'r' + ending
                return data 
            if ending[0] == 's' and ending[1] == 's':
                data = prefix + ending
                return data 
            elif ending[0] == 's':
                data = prefix + 's' + ending
                return data 
            elif ending[0] == 'h':
                data = prefix + ending[1:]
                return data 
            else:
                data = prefix + ending
                return data 
        
        def prefixRe(prefix, ending):
            data = prefix + ending
            return data

        def prefixNao(prefix, ending):
            data = prefix + ' ' + ending
            return data

        def prefixDesIn(prefix, ending):
            if ending[0] == 'h':
                data = prefix + ending[1:]
                return data
            else:
                data = prefix + ending
                return data
        
        def prefixBem(prefix, ending):
            data = prefix + '-' + ending
            data_exception = prefix[:2] + 'n' + ending
            if ending == 'feitor':
                return data_exception
            elif ending == 'feito':
                return data_exception
            else:
                return data

        def prefixSubSob(prefix, ending):
            if ending[0] == 'b':
                data = prefix + '-' + ending
                return data
            elif ending[0] == 'r':
                data = prefix + '-' + ending
                return data
            elif 'human' in ending:
                data = prefix + ending[1:]
                return data
            elif ending[0] == 'h':
                data = prefix + '-' + ending
                return data
            else:
                data = prefix + ending
                return data

        def prefixSmall(prefix, ending):
            if ending[0] == 'r':
                data = prefix + '-' + ending
                return data
            else:
                data = prefix + ending
                return data

        def prefixNumber(prefix, ending):
            data = prefix + ending
            return data

        def prefixEr(prefix, ending):
            if ending[0] == 'h':
                data = prefix + '-' + ending
                return data
            elif ending[0] == 'r':
                data = prefix + '-' + ending
                return data
            else:
                data = prefix + ending
                return data

        def prefixCircumPan(prefix, ending):
            if ending[0] == 'h':
                data = prefix + '-' + ending
                return data
            elif ending[0] == 'n':
                data = prefix + '-' + ending
                return data
            elif ending[0] == 'm':
                data = prefix + '-' + ending
                return data
            else:
                data = prefix + ending
                return data

        def prefixHyphenated(prefix, ending):
            data = prefix + '-' + ending
            return data
        
        def prefixMal(prefix, ending):
            if ending[0] in vowels:
                data = prefix + '-' + ending
                return data
            elif ending[0] in letters:
                data = prefix + '-' + ending
                return data
            else:
                data = prefix + ending
                return data
        
        def prefixPseudoprefix(prefix, ending):
            if prefix[-1] in vowels and ending[0] in vowels:
                if prefix[-1] in vowel_a and ending[0] in vowel_a:
                    data =  prefix + '-' + ending
                    return data
                elif prefix[-1] in vowel_e and ending[0] in vowel_e:
                    data =  prefix + '-' + ending
                    return data
                elif prefix[-1] in vowel_i and ending[0] in vowel_i:
                    data =  prefix + '-' + ending
                    return data
                elif prefix[-1] in vowel_o and ending[0] in vowel_o:
                    data =  prefix + '-' + ending
                    return data
                elif prefix[-1] in vowel_u and ending[0] in vowel_u:
                    data =  prefix + '-' + ending
                    return data
                else:
                    data =  prefix + ending
                    return data

            elif ending[0] == 'h':
                data =  prefix + '-' + ending
                return data
            
            elif prefix[-1] in vowels and ending[0] == 'r' and ending[1] == 'r':
                # if words[1][0] == 'r' and words[1][1] == 'r':
                data =  prefix + ending
                return data

            elif prefix[-1] in vowels and ending[0] == 'r':
                data =  prefix + 'r' + ending
                return data


            elif prefix[-1] in vowels and ending[0] == 's' and ending[1] == 's':
                data =  prefix + ending
                return data   


            elif prefix[-1] in vowels and ending[0] == 's':
                data =  prefix + 's' + ending
                return data

            else:
                data = prefix + ending
                return data

        def prefixes(validation, words, ending):
            if validation == 'prefixo':
                if words in prefix_co:
                    data = prefixCo(words, ending)
                    return data
                
                elif words in prefix_re:
                    data = prefixRe(words, ending)
                    return data

                elif words in prefixes_des_in:
                    data = prefixDesIn(words, ending)
                    return data
                
                elif words in prefix_nao:
                    data = prefixNao(words, ending)
                    return data

                elif words in prefix_bem:
                    data = prefixBem(words, ending)
                    return data
                
                elif words in prefixes_sub_sob:
                    data = prefixSubSob(words, ending)
                    return data

                elif words in pseudoprefixes_number:
                    data = prefixNumber(words, ending)
                    return data
                elif words in prefixes_small:
                    data = prefixSmall(words, ending)
                    return data                    
                elif words in prefixes_er:
                    data = prefixEr(words, ending)
                    return data
                elif words in prefixes_circum_pan:
                    data = prefixCircumPan(words, ending)
                    return data
                elif words in prefixes_hyphenated:
                    data = prefixHyphenated(words, ending)
                    return data
                elif words in prefix_mal:
                    data = prefixMal(words, ending)
                    return data
                elif words in prefixes_default or pseudoprefixes:
                    data = prefixPseudoprefix(words, ending)
                    return data

                else:
                    return 'not prefix'

            elif compound_hyphenating == 'error hyphenating':
                return 'error'
            else:
                return compound_hyphenating

        answer = prefixes(compound_hyphenating, words[0], words[1])
        return answer      

    correct_word = hyphenating(list_words)

    return correct_word

view = hifenizei('mal estar')
print(view)

# verificar malestar
# inserir secondWords para prefixes_small e prefixo 'meso'
# ver flexão de gênero e número
# classificar palavras que sejam nomes de animais ou plantas


            




            
