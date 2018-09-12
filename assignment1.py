import nltk
import collections
import math
from nltk.tokenize import sent_tokenize, word_tokenize

path = 'train/obama.txt'
obama_file = open(path,'r')
days = obama_file.read()
# print(word_tokenize(days))

length = len(word_tokenize(days))
print(length)

# find the occurences of each word (dictionary)
word = word_tokenize(days)
counts = collections.Counter(word)
# print(counts)

# update dictionary containing probability as the values - unigram
for key, value in counts.items():
    counts[key] = value / length
print(counts)
# print(counts.values())
# val = max(counts.values())
# print(val)

###get rid of the punctuation???? --------------------

# find bigram