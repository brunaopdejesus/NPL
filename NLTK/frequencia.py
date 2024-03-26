import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')

texto = "O cachorro correu pelo parque. O gato dormiu na poltrona. O cachorro latiu para o gato."

tokens = word_tokenize(texto.lower(), language='portuguese')

pontuacao = set(string.punctuation)
stop_words = set(stopwords.words('portuguese'))
tokens_filtrados = [word for word in tokens if word not in pontuacao and word not in stop_words]

frequencia = Counter(tokens_filtrados)

print("Frequência das palavras: ")
for palavra, freq in frequencia.items():
    print(f"{palavra}: {freq}")