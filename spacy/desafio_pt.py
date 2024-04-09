import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Carregar o modelo em português do spaCy
nlp = spacy.load('pt_core_news_sm')
nlp.add_pipe('spacytextblob')

def analyze_sentiment(text):
    doc = nlp(text)
    polarity = doc._.blob.polarity

    # Definir o limite para a margem de neutralidade
    neutral_margin = 0.2

    # Definir o limite para polaridade negativa
    negative_limit = -0.5

    # Determinar se a frase é positiva, negativa ou neutra com base na polaridade
    if polarity > neutral_margin:
        sentiment = "positiva"
    elif polarity < negative_limit:
        sentiment = "negativa"
    else:
        sentiment = "neutra"
    
    return polarity, sentiment

# Frases para teste em português
texts = [
    "Tive um dia terrível. Foi o pior dia de todos! Mas de vez em quando eu tenho um dia muito bom que me deixa feliz.",
    "O tempo hoje não está nem bom nem ruim. Está apenas médio.",
    "Estou extasiado com as notícias! É o melhor dia de todos!",
    "Não tenho certeza do que sinto sobre isso. Está tudo bem, eu acho.",
    "Não consigo conter minha empolgação! Isso é incrível!",
    "Estou extremamente decepcionado com o serviço que recebi no restaurante. A comida estava fria, os funcionários foram rudes e a experiência geral foi terrível."
]

# Analisar o sentimento de cada frase em português
for i, text in enumerate(texts):
    polarity, sentiment = analyze_sentiment(text)
    print(f"Sentimento da frase {i+1}: {sentiment} (Polaridade: {polarity})")
