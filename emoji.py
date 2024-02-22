dicionario_sentimentos = {
    "positivo": ["😊", "❤", "😍", "👌", "😁"],
    "negativo": ["🤬", "😡", "😠", "🙁", "😭"]
}

def analisar_frase(frase, dicionario):
    palavras = frase.lower().split()
    contador = {"positivo": sum(palavra in dicionario["positivo"] for palavra in palavras),
                "negativo": sum(palavra in dicionario["negativo"] for palavra in palavras)}
    return "Positivo" if contador["positivo"] > contador["negativo"] else "Negativo" if contador["positivo"] < contador["negativo"] else "Neutro"

frase_usuario = input("Digite uma frase: ")
sentimento_frase = analisar_frase(frase_usuario, dicionario_sentimentos)
print("O sentimento da frase é:", sentimento_frase)