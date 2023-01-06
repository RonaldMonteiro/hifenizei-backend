import nltk

nltk.download('punkt')


with open('functions/functions/corpora/prefixes.txt', mode='r', encoding='utf-8') as corporaPrefixes:
    prefixesReading = corporaPrefixes.read()

with open('functions/functions/corpora/pseudoprefixes.txt', mode='r', encoding='utf-8') as corporaPseudoprefixes:
    pseudoprefixesReading = corporaPseudoprefixes.read()

with open('functions/corpora/prefixes_hyphenated.txt', mode='r', encoding='utf-8') as corporaPrefixesHyphenated:
    prefixesHyphenatedReading = corporaPrefixesHyphenated.read()

with open('functions/corpora/prefixes_small.txt', mode='r', encoding='utf-8') as corpora_prefixesSmall:
    prefixesSmall_reading = corpora_prefixesSmall.read()

with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as corpora_compound_word:
    compound_word_reading = corpora_compound_word.read()

with open('functions/corpora/compound_copy.txt', mode='r', encoding='utf-8') as corpora_compound_copy:
    compound_copy_reading = corpora_compound_copy.read()

def part_compound_words(compoundWordsTuplas):
    prefixes_compound = []
    for (w,t) in compoundWordsTuplas:
        prefixes_compound.append(w)
    return prefixes_compound



prefixes_default = nltk.tokenize.word_tokenize(prefixesReading)

pseudoprefixes = nltk.tokenize.word_tokenize(pseudoprefixesReading)

prefixes_hyphenated = nltk.tokenize.word_tokenize(prefixesHyphenatedReading)

prefixes_small = nltk.tokenize.word_tokenize(prefixesSmall_reading)

compound_words = nltk.tokenize.word_tokenize(compound_word_reading)

compound_words_tuplas = [nltk.tag.str2tuple(word) for word in compound_words]

words_parts = part_compound_words(compound_words_tuplas)

compound_copy = nltk.tokenize.word_tokenize(compound_copy_reading)

letters = ['h', 'l']

vowel_a = ['a','á','â']
vowel_e = ['e','é','ê']
vowel_i = ['i','í','î']
vowel_o = ['o','ó','ô']
vowel_u = ['u','ú','û']
vowels = ['a','e','i','o','u','á','é','í','ó','ú','â','ê','î','ô','û']

prefix_mal = ['mal']

prefix_co = ["co"]

prefix_re = ['re']

prefix_bem = ['bem', 'ben']

prefixes_des_in = ['des','in']

prefix_nao = ['não']

prefixes_sub_sob = ['sub','sob']

prefixes_circum_pan = ['circum','pan']

pseudoprefixes_number = ['bi','tri','tetra','penta','hexa']

prefixes_er = ['hiper','inter','super']

all_prefixes = (prefix_nao + prefixes_circum_pan + prefixes_des_in + prefixes_er 
+ pseudoprefixes_number + prefixes_sub_sob + prefixes_default + prefix_bem + prefix_co + 
prefix_re + pseudoprefixes + prefixes_hyphenated + prefixes_small + 
prefix_mal) #sem palavras convencionais
all_words = words_parts + all_prefixes

listException = []
with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as x:
    xx = x.readlines()
    for line in xx:
        if '#' in line[0]:
            listException.append(nltk.tokenize.word_tokenize(line))

listExceptionClean =[]
for group in listException:
    listExceptionClean.append(group[1])

list_exception =[]
for word in listExceptionClean:
    list_exception.append(word.split('/'))

listPhrase = []
with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as x:
    xx = x.readlines()
    for line in xx:
        if '*' in line[0]:
            listPhrase.append(nltk.tokenize.word_tokenize(line))

listPhraseClean =[]
for group in listPhrase:
    listPhraseClean.append(group[1])

list_phrase =[]
for word in listPhraseClean:
    list_phrase.append(word.split('/'))


listRepet = []
with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as x:
    xx = x.readlines()
    for line in xx:
        if '@' in line[0]:
            listRepet.append(nltk.tokenize.word_tokenize(line))

listRepetClean =[]
for group in listRepet:
    listRepetClean.append(group[1])

list_repet =[]
for word in listRepetClean:
    list_repet.append(word.split('/'))


with open('functions/functions/corpora/prefixesSeconds.txt', mode='r', encoding='utf-8') as prefixesSecondsCorpora:
    prefixesSecondsReading = prefixesSecondsCorpora.read()



all_terms = nltk.tokenize.word_tokenize(prefixesSecondsReading)

# with open('backend/functions/corpora/wordsSeconds.txt', mode='r', encoding='utf-8') as WordsSecondsCorpora:
#     WordsSecondsReading = WordsSecondsCorpora.read()

# WordsSeconds = nltk.tokenize.word_tokenize(WordsSecondsReading)


