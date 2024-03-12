import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

text = "O novo livro do autor será lançado em breve na feira do livro."

words = word_tokenize(text, language='portuguese')

lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

lemmatized_text = ' '.join(lemmatized_words)

print("Texto original:")
print(text)
print("\nTexto com lematização:")
print(lemmatized_text)
