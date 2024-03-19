import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import opinion_lexicon
 
# Baixe os recursos necessários da NLTK (stopwords e punkt)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('opinion_lexicon')
 
# Carregue o dicionário de palavras positivas e negativas da NLTK
palavras_positivas = set(opinion_lexicon.positive())
palavras_negativas = set(opinion_lexicon.negative())
 
# Função para pré-processar o texto
def preprocessamento(texto):
    # Converte o texto para minúsculas
    texto = texto.lower()
    # Tokeniza o texto em palavras
    tokens = word_tokenize(texto)
    # Remove stopwords e pontuações
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('portuguese')]
    return tokens
 
# Função para analisar o sentimento da opinião considerando o contexto das palavras
def analisar_sentimento_v2(opiniao):
    tokens = preprocessamento(opiniao)
    sentimento = 0
   
    for i, token in enumerate(tokens):
        if token in palavras_positivas:
            if i > 0 and tokens[i - 1] == 'não':  # Se a palavra anterior for 'não', inverte o sentimento
                sentimento -= 1
            else:
                sentimento += 1
        elif token in palavras_negativas:
            if i > 0 and tokens[i - 1] == 'não':  # Se a palavra anterior for 'não', inverte o sentimento
                sentimento += 1
            else:
                sentimento -= 1
   
    if sentimento > 0:
        return "positivo"
    elif sentimento < 0:
        return "negativo"
    else:
        return "neutro"
 
# Exemplos de opiniões
dicionarioComentarios = {
    "comentario1": "Lindo por demais, acabei de receber mas ainda não usei, mas pelo valor parece ser um ótimo custo benefício. *** agora voltando para opinar sobre e liquidificador, perfeito, ótimo custo benefício, bate muiiito, não cheira queimado nenhum como alguns falam. Está à procura de um ótimo liquidificador e não quer ou não pode investir mais que esse valor? então esse é o cara, recomendo e não irás se arrepender, grato.",
    "comentario2": "Muito bom. Tritura coisa pra caramba de uma vez, incluindo beterraba e cenoura. Estou fazendo altos sucos! hihi faz um barulho normal de liquidificador, é fácil de limpar, n sobe cheiro de queimado tão rápido (até agora não subiu). A única coisa ligeiramente chatinha mas q não interfere tanto é que vaza um pouco. Mas é coisa bem pouca. Sempre quando acabo de bater, ficam diversas gotas de qualquer coisa que eu tô fazendo na parte de cima do motor, mas é só passar um papel que seca rapidinho. Até agora isso não deu nenhuma interferência e acho que não vai dar, as gotas só ficam na bordinha mesmo. Um bom liquidificador!",
    "comentario3": "Comprei mas bem com o pé atrás por causa de alguns comentários falando que não era bom mas comprei assim mesmo pois minha mãe já teve um desses e eu só confiei. É muito bom, potente, bate muito bem de sucos até bolos. Fora que é lindo , e o filtro facilita demais na hora de coar sucos, muito satisfeita com a compra. Podem comprar de olhos fechados.",
    "comentario4": "O liquidificador desde o primeiro uso fica com cheiro de queimado, então eu tenho medo de deixar ele ligado durante muito tempo, e o copo vaza um pouco em baixo, comprei na voltagem certa pra minha casa então não tem como ser culpa da voltagem, por enquanto tá funcionando kkkkkkl msm eu com medo de usar. Bom voltei, usei o liquidificador umas 10 vezes e ele queimou, desde o começo já apresentava falhas, dinheiro jogado fora infelizmente.",
    "comentario5": "Bom! pelo valor achei exelente, o copo é so colocar sobre a base que já encaixa, gostei dessa praticidade, tem um desingner bonito, o encaixe da tampa é perfeito, não é muito barulhento e tritura alguns alimento com um pouco de dificuldade, mas se deixar por um pouco mais de tempo tritura tudo.",
    "comentario6": "Pela primeira vez precisei usar o produto para bater várias coisas um absurdo não presta começou a fumacar nem consegui terminar não presta de jeito nenhum horrível 0 nota não comprem. Um lixo levei na assistência",
    "comentario7": "Uma porcaria não funciona não comprem nessa loja é uma loja golpista estou tentando me roubar me venderam esse produto sem que funcione e não querem me devolver o dinheiro e o mercado livre está sendo cúmplice disso.",
    "comentario8": "Eu super recomendo, pois já tinha comprado uns três liquidificador e não prestou tudo fraco, esse da mondial eu amei adorei e muito lindo e muito potente. Comprem sem medo.",
    "comentario9": "Achei mediano. O filtro fica solto, não encaixa direito. E dependendo da velocidade que estiver usando tem que ficar segurando a tampa principalmente com o filtro que fica muito rente a tampa, caso contrário a tampa sai. O ponto positivo é que ele é potente e atende as minhas necessidades nesse momento. O único problema pra mim foi o filtro mesmo.",
    "comentario10": "Olha comprei para dar de presente, mais a pessoa que presenteie disse que sempre que vai usar sobe um cheiro de queimado aí ela desliga rápido para não queimar, vamos ver quanto tempo vai durar assim neh."
}
 
# Analisando os sentimentos das opiniões
for comentario, opiniao in dicionarioComentarios.items():
    print(f"{comentario}: {analisar_sentimento_v2(opiniao)}")

# Comentários retirados do site do Mercado Livre:
# https://www.mercadolivre.com.br/liquidificador-mondial-l-99-500w-22l-c-jarra-san-pt-110v/p/MLB15578949#reviews
