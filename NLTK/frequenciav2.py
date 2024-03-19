import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string
import matplotlib.pyplot as plt

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

plt.figure(figsize=(12,6))
plt.bar(frequencia.keys(), frequencia.values())
plt.xticks(rotation=45)
plt.xlabel('Palavra')
plt.ylabel('Frequência')
plt.title('Frequência das palavras no texto')
plt.show()

plt.figure(figsize=(8,8))
plt.pie(frequencia.values(), labels = frequencia.keys(), autopct='%1.1fNX')
plt.title('Distribuição das palavras no texto')
plt.show() 
