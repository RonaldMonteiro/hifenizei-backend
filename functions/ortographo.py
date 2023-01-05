# import nltk
# import nltk.tokenize
# from nltk.corpus import floresta, mac_morpho
# import heapq
# from corpora.corpora import *
# # mac = mac_morpho.words()

# # def clear_characters(tokens):
# #     alpha_tokens = []
# #     clean_tokens = []
# #     for token in tokens:
# #         if token.isalpha():
# #             alpha_tokens.append(token)
# #     for alpha_token in alpha_tokens:
# #         clean_tokens.append(alpha_token.lower())
# #     return clean_tokens

# # clean_tokens = clear_characters(tokens)

# # def frequency(created_word):
# #     frequency = nltk.FreqDist(clean_tokens)
# #     all_words = len(clean_tokens)
# #     return frequency[created_word] / all_words

# def invert_letters(word):
#     def posting_letters(parts):
#         unknown_words = []
#         letters = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
#         for _left, _right in parts:
#             for letra in letters:
#                 unknown_words.append(_left + letra + _right)
#         return unknown_words


#     def excluding_letters(parts):
#         unknown_words = []
#         for _left, _right in parts:
#             unknown_words.append(_left + _right[1:])
#         return unknown_words

#     def changing_letters(parts):
#         unknown_words = []
#         letters = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
#         for _left, _right in parts:
#             for letra in letters:
#                 unknown_words.append(_left + letra + _right[1:])
#         return unknown_words


#     def inverting_letters(parts):
#         unknown_words = []
#         for _left, _right in parts:
#             if len(_right) > 1:
#                 unknown_words.append(_left + _right[1] + _right[0] + _right[2:])
#         return unknown_words
#     parts = []
#     v = 0
#     for v in range(len(word) + 1):
#         parts.append((word[:v], word[v:]))
#     created_words = posting_letters(parts)
#     created_words += excluding_letters(parts)
#     created_words += changing_letters(parts)
#     created_words += inverting_letters(parts)
#     return created_words

# entry = 'impeialístico'
# list_words = invert_letters(entry)

# for word in set(all_terms):
#     if word in set(list_words):
#         data = word
#         print(data)
# else:
#     pass
# # listaWord = []
# # for prefix in all_prefixes:
# #     if len(prefix) > 4:
# #         listaWord.append(prefix)

# # print(len(listaWord), len(all_prefixes))
        

# # def distance_letters(created_words):
# #     unknown_words = []
# #     for word in created_words:
# #         unknown_words += invert_letters(word)
# #     return unknown_words

# # def aspirant_generator(wrong_word):
# #     vocabulary = set(clean_tokens)
# #     invert_letter = invert_letters(wrong_word)
# #     distance_letter = distance_letters(invert_letter)
# #     all_words = set(invert_letter + distance_letter)
# #     aspirants_words = [wrong_word]
# #     for word in all_words:
# #         if word in vocabulary:
# #             aspirants_words.append(word)
# #     return aspirants_words





# # def probability(word):
# #     frequency = nltk.FreqDist(clean_tokens)
# #     return frequency[word]
  

# # def probability_list(possibilitys_words):
# #     probability_words = []
# #     for word in possibilitys_words:
# #         number = probability(word)
# #         probability_words.append((word,number))
# #     probability_words.sort(key=lambda x: x[1])
# #     return probability_words


# # def reducing_list(probability_tuplas):
# #     v = len(probability_tuplas) / 2
# #     reduce_list = heapq.nlargest (int(v), probability_tuplas)
# #     return reduce_list


# # def distance_list(reduce_list):
# #     distance_words = []
# #     list_words = []
# #     for (word, number) in reduce_list:
# #         list_words.append(word)
# #     for word in list_words:
# #         number = nltk.jaccard_distance(set(_input), set(word))
# #         distance_words.append((word, number))
# #     distance_words.sort(key=lambda x: x[1])
# #     return distance_words 

# # while print:
# #     _input = input("digite uma palavra: ")
# #     possibilitys_words = aspirant_generator(_input)
# #     probability_tuplas = probability_list(possibilitys_words)
# #     reduce_list = reducing_list(probability_tuplas)
# #     print(possibilitys_words)

# # ao gerar uma grande lista de dados desordenados, 
# # o programa saberá que a string correta é aquela que está limitada aos ending
# # um grande corpus não é necessário