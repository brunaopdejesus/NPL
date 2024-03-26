import nltk
from nltk.tree import Tree

def extrair_arvore_sintatica(frase):
    # Tokenizar a frase em palavras
    palavras = nltk.word_tokenize(frase)
    # Realizar análise sintática
    parser = nltk.ChartParser()
    arvore = next(parser.parse(palavras))
    return arvore

def exibir_arvore_sintatica_visual(arvore):
    # Exibir a árvore sintática de forma visualmente mais atraente
    print(arvore.pretty_print())

def main():
    # Frase de exemplo
    frase = "O gato pulou o muro."
    # Extrair a árvore sintática da frase
    arvore_sintatica = extrair_arvore_sintatica(frase)
    # Exibir a árvore sintática visualmente
    print("Árvore Sintática:")
    exibir_arvore_sintatica_visual(arvore_sintatica)

if __name__ == "__main__":
    main()