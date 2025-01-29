import nltk
nltk.download('averaged_perceptron_tagger_eng')
from textblob import TextBlob
text= 'I love programming'

blob= TextBlob(text)
print('Sentiment:', blob.sentiment)

print('original text:', text)
print('corrected text:', blob.correct())
print('tags:', blob.tags)
print('noun phrases:', blob.noun_phrases)
print('words:', blob.words)
print('sentences:', blob.sentences)
print('language:', blob.detect_language())
print('translation:', blob.translate(to='de'))
print('polarity:', blob.sentiment.polarity)