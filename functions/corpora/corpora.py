import nltk

nltk.download('punkt')


with open('functions/corpora/prefixes.txt', mode='r', encoding='utf-8') as corporaPrefixes:
    prefixesReading = corporaPrefixes.read()

prefixes = nltk.tokenize.word_tokenize(prefixesReading)

with open('functions/corpora/pseudoprefixes.txt', mode='r', encoding='utf-8') as corporaPseudoprefixes:
    pseudoprefixesReading = corporaPseudoprefixes.read()

pseudoprefixes = nltk.tokenize.word_tokenize(pseudoprefixesReading)

with open('functions/corpora/prefixes_hyphenated.txt', mode='r', encoding='utf-8') as corporaPrefixesHyphenated:
    prefixesHyphenatedReading = corporaPrefixesHyphenated.read()

prefixesHyphenated = nltk.tokenize.word_tokenize(prefixesHyphenatedReading)

with open('functions/corpora/prefixes_small.txt', mode='r', encoding='utf-8') as corpora_prefixesSmall:
    prefixesSmall_reading = corpora_prefixesSmall.read()

prefixesSmall = nltk.tokenize.word_tokenize(prefixesSmall_reading)

with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as corpora_compound_word:
    compound_word_reading = corpora_compound_word.read()

compound_words = nltk.tokenize.word_tokenize(compound_word_reading)

compoundWordsTuplas = [nltk.tag.str2tuple(word) for word in compound_words]

def part_compound_words(compoundWordsTuplas):
    prefixes_compound = []
    for (w,t) in compoundWordsTuplas:
        prefixes_compound.append(w)
    return prefixes_compound

wordsParts = part_compound_words(compoundWordsTuplas)


with open('functions/corpora/compound_copy.txt', mode='r', encoding='utf-8') as corpora_compound_copy:
    compound_copy_reading = corpora_compound_copy.read()

compound_copy = nltk.tokenize.word_tokenize(compound_copy_reading)

h_and_l = ['h', 'l']

vowels = ['a','e','i','o','u']

prefixSpecial = ['mal']

prefixCo = ["co"]

prefixRe = ['re']

prefixBem = ['bem']

prefixDesIn = ['des','in']

prefixNao = ['não']

prefixSubSob = ['sub','sob']

prefixCircumPan = ['circum','pan']

pseudoprefixesNumber = ['bi','tri','tetra','penta','hexa']

prefixEr = ['hiper','inter','super']

allPrefixes = (prefixNao + prefixCircumPan + prefixDesIn + prefixEr 
+ pseudoprefixesNumber + prefixSubSob + prefixes + prefixBem + prefixCo + 
prefixRe + pseudoprefixes + prefixesHyphenated + prefixesSmall + 
prefixSpecial + wordsParts)

listException = []
with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as x:
    xx = x.readlines()
    for line in xx:
        if '#' in line[0]:
            listException.append(nltk.tokenize.word_tokenize(line))

listExceptionClean =[]
for group in listException:
    listExceptionClean.append(group[1])

listExceptionNormalization =[]
for word in listExceptionClean:
    listExceptionNormalization.append(word.split('/'))

listPhrase = []
with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as x:
    xx = x.readlines()
    for line in xx:
        if '*' in line[0]:
            listPhrase.append(nltk.tokenize.word_tokenize(line))

listPhraseClean =[]
for group in listPhrase:
    listPhraseClean.append(group[1])

listPhraseNormalization =[]
for word in listPhraseClean:
    listPhraseNormalization.append(word.split('/'))


listRepet = []
with open('functions/corpora/compound_words.txt', mode='r', encoding='utf-8') as x:
    xx = x.readlines()
    for line in xx:
        if '@' in line[0]:
            listRepet.append(nltk.tokenize.word_tokenize(line))

listRepetClean =[]
for group in listRepet:
    listRepetClean.append(group[1])

listRepetNormalization =[]
for word in listRepetClean:
    listRepetNormalization.append(word.split('/'))


with open('functions/corpora/prefixesSeconds.txt', mode='r', encoding='utf-8') as prefixesSecondsCorpora:
    prefixesSecondsReading = prefixesSecondsCorpora.read()



prefixesSecondss = nltk.tokenize.word_tokenize(prefixesSecondsReading)

with open('functions/corpora/wordsSeconds.txt', mode='r', encoding='utf-8') as WordsSecondsCorpora:
    WordsSecondsReading = WordsSecondsCorpora.read()

WordsSeconds = nltk.tokenize.word_tokenize(WordsSecondsReading)

prefixesSeconds = prefixesSecondss + WordsSeconds

