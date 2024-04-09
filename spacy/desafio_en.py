import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
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

# Frases para teste
texts = [
    "I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.",
    "The weather today is neither good nor bad. It's just average.",
    "I'm feeling ecstatic about the news! It's the best day ever!",
    "I'm not sure how I feel about this. It's okay, I guess.",
    "I can't contain my excitement! This is amazing!",
    "I'm extremely disappointed with the service I received at the restaurant. The food was cold, the staff was rude, and the overall experience was terrible."
]

# Frase negativa
text_negative = "I'm extremely disappointed with the service I received at the restaurant. The food was cold, the staff was rude, and the overall experience was terrible."

# Analisar o sentimento de cada frase
for i, text in enumerate(texts):
    polarity, sentiment = analyze_sentiment(text)
    print(f"Sentimento da frase {i+1}: {sentiment} (Polaridade: {polarity})")

