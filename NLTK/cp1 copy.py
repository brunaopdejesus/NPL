import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixe os recursos necessários do NLTK (caso ainda não tenha feito isso)
nltk.download('punkt')
nltk.download('vader_lexicon')

# Função para analisar o sentimento usando VADER
def analisar_sentimento_vader(texto):
    sia = SentimentIntensityAnalyzer()
    sentimento = sia.polarity_scores(texto)
    return sentimento

# Palavras-chave para sentimento positivo e negativo
palavras_positivas = ["bom", "ótimo", "excelente", "maravilhoso", "adorável", "satisfeito", "recomendo"]
palavras_negativas = ["ruim", "péssimo", "horrível", "desapontado", "insatisfeito", "odioso", "detestei"]

# Exemplos de opiniões
dicionarioComentarios = {
    "comentario1": "Lindo por demais, acabei de receber mas ainda não usei, mas pelo valor parece ser um ótimo custo benefício.",
    "comentario2": "Muito bom. Tritura coisa pra caramba de uma vez, incluindo beterraba e cenoura.",
    "comentario3": "Comprei mas bem com o pé atrás por causa de alguns comentários falando que não era bom mas comprei assim mesmo pois minha mãe já teve um desses e eu só confiei.",
    "comentario4": "O liquidificador desde o primeiro uso fica com cheiro de queimado, então eu tenho medo de deixar ele ligado durante muito tempo.",
    "comentario5": "Bom! pelo valor achei excelente, o copo é só colocar sobre a base que já encaixa, gostei dessa praticidade.",
    "comentario6": "Pela primeira vez precisei usar o produto para bater várias coisas um absurdo não presta começou a fumacar nem consegui terminar não presta de jeito nenhum horrível 0 nota não comprem.",
    "comentario7": "Uma porcaria não funciona não comprem nessa loja é uma loja golpista estou tentando me roubar me venderam esse produto sem que funcione e não querem me devolver o dinheiro e o mercado livre está sendo cúmplice disso.",
    "comentario8": "Eu super recomendo, pois já tinha comprado uns três liquidificador e não prestou tudo fraco, esse da mondial eu amei adorei e muito lindo e muito potente. Comprem sem medo."
}

# Analisando os sentimentos das opiniões usando VADER
for comentario, opiniao in dicionarioComentarios.items():
    resultado = analisar_sentimento_vader(opiniao)
    score_positivo = sum(resultado[p] for p in resultado if p in palavras_positivas)
    score_negativo = sum(resultado[n] for n in resultado if n in palavras_negativas)
    score_neutro = resultado['neu']
    print(f"{comentario}:")
    print(f"Score de positividade: {score_positivo}")
    print(f"Score de negatividade: {score_negativo}")
    print(f"Score de neutralidade: {score_neutro}")
    print()
