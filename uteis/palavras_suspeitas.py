import json


def detector_palavras(texto):
    with open("dados/palavras_chaves.json", "r") as arquivo:
        palavras_chaves = json.load(arquivo)


    score = 0
    motivos = []
    for categoria, lista_palavras in palavras_chaves.items():
        for palavras in lista_palavras:
            if palavras in texto:
                score = 3
                motivos.append(f"Item suspeito [{palavras}] da categoria [{categoria}]")
                
    
    resultado = {
        "score":score,
        "motivos":motivos
    }
                
    return resultado
        


