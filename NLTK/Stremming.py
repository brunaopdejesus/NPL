import nltk
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize

nltk.download('rslp')

stemmer = RSLPStemmer()

text = "Eu estava pensando que poderia ter sido melhor."

words = word_tokenize(text, language='portuguese')

stemmed_words = [stemmer.stem(word) for word in words]

stemmed_text = ' '.join(stemmed_words)

print("Texto original:")
print(text)
print("\nTexto com stemming:")
print(stemmed_text)
