from translate import Translator

translator= Translator(to_lang='de')

text= 'hello, good morning'

translation= translator.translate(text)

print('translated text:', translation)
