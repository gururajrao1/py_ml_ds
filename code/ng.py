import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
sentence= "guten morgen herr gururaj"
tokens= word_tokenize(sentence)
bigrams = list(ngrams(tokens,2)) #bigrams
trigrams= list(ngrams(tokens,3)) #trigrams
unigrams = list(ngrams(tokens,1)) #unigrams

print(bigrams)
print(unigrams)
print(trigrams)