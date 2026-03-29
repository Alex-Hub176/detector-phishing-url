import json


def detector_palavras(texto):
    with open("dados/palavras_chaves.json", "r") as arquivo:
        palavras_chaves = json.load(arquivo)

    for categoria, lista_palavras in palavras_chaves.items():
        for palavras in lista_palavras:
            if palavras in texto:
                return 3
                
        


