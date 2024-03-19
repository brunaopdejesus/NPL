# Dicionário manual de palavras positivas e negativas
palavras_positivas = {"bom", "ótimo", "excelente", 
                     "legal", "maneiro", "ok", 
                     "foda", "divertido", "interessante", 
                     "incrível", "perfeito", "útil",
                     "recomendo", "custo", "benefício", "lindo",
                     "fácil", "bonito", "prático",
                     "potente", "satisfeita"}
palavras_negativas = {"ruim", "péssimo", "terrível", 
                      "horrível", "ridículo", "horroroso",
                      "chato", "paia", "merda",
                      "cheiro", "queimado", "medo", "falhas", "dinheiro", "jogado", "fora",
                      "absurdo", "fumando", "lixo", "não", "presta", "0", "nota",
                      "porcaria", "golpista", "roubar", "cúmplice", 
                      "solto", "problema"}

# Função para pré-processar o texto (remover pontuações e converter para minúsculas)
def preprocessamento(texto):
    texto = texto.lower()
    texto = texto.replace(',', '').replace('.', '')  # Remover pontuações
    return texto

# Função para analisar o sentimento da opinião
def analisar_sentimento(opiniao):
    opiniao = preprocessamento(opiniao)
    tokens = opiniao.split()
   
    # Verificar se há palavras positivas ou negativas na opinião
    if any(token in palavras_positivas for token in tokens):
        return "positivo"
    elif any(token in palavras_negativas for token in tokens):
        return "negativo"
    else:
        return "neutro"

# Dicionário de comentários
dicionarioComentarios = {
    "comentario1": "Lindo por demais, acabei de receber mas ainda não usei, mas pelo valor parece ser um ótimo custo benefício. *** agora voltando para opinar sobre e liquidificador, perfeito, ótimo custo benefício, bate muiiito, não cheira queimado nenhum como alguns falam. Está à procura de um ótimo liquidificador e não quer ou não pode investir mais que esse valor? então esse é o cara, recomendo e não irás se arrepender, grato.",
    "comentario2": "Muito bom. Tritura coisa pra caramba de uma vez, incluindo beterraba e cenoura. Estou fazendo altos sucos! hihi faz um barulho normal de liquidificador, é fácil de limpar, n sobe cheiro de queimado tão rápido (até agora não subiu). A única coisa ligeiramente chatinha mas q não interfere tanto é que vaza um pouco. Mas é coisa bem pouca. Sempre quando acabo de bater, ficam diversas gotas de qualquer coisa que eu tô fazendo na parte de cima do motor, mas é só passar um papel que seca rapidinho. Até agora isso não deu nenhuma interferência e acho que não vai dar, as gotas só ficam na bordinha mesmo. Um bom liquidificador!",
    "comentario3": "Comprei mas bem com o pé atrás por causa de alguns comentários falando que não era bom mas comprei assim mesmo pois minha mãe já teve um desses e eu só confiei. É muito bom, potente, bate muito bem de sucos até bolos. Fora que é lindo , e o filtro facilita demais na hora de coar sucos, muito satisfeita com a compra. Podem comprar de olhos fechados.",
    "comentario4": "Bom! pelo valor achei exelente, o copo é so colocar sobre a base que já encaixa, gostei dessa praticidade, tem um desingner bonito, o encaixe da tampa é perfeito, não é muito barulhento e tritura alguns alimento com um pouco de dificuldade, mas se deixar por um pouco mais de tempo tritura tudo.",
    "comentario5": "Pela primeira vez precisei usar o produto para bater várias coisas um absurdo não presta começou a fumacar nem consegui terminar não presta de jeito nenhum horrível 0 nota não comprem. Um lixo levei na assistência",
    "comentario6": "Uma porcaria não funciona não comprem nessa loja é uma loja golpista estou tentando me roubar me venderam esse produto sem que funcione e não querem me devolver o dinheiro e o mercado livre está sendo cúmplice disso.",
    "comentario7": "Eu super recomendo, pois já tinha comprado uns três liquidificador e não prestou tudo fraco, esse da mondial eu amei adorei e muito lindo e muito potente. Comprem sem medo.",
    "comentario8": "Achei mediano. O filtro fica solto, não encaixa direito. E dependendo da velocidade que estiver usando tem que ficar segurando a tampa principalmente com o filtro que fica muito rente a tampa, caso contrário a tampa sai. O ponto positivo é que ele é potente e atende as minhas necessidades nesse momento. O único problema pra mim foi o filtro mesmo.",
    "comentario9": "Olha comprei para dar de presente, mais a pessoa que presenteie disse que sempre que vai usar sobe um cheiro de queimado aí ela desliga rápido para não queimar, vamos ver quanto tempo vai durar assim neh."
}

# Analisando os sentimentos das opiniões
for comentario, opiniao in dicionarioComentarios.items():
    print(f"{comentario}: {analisar_sentimento(opiniao)}")

