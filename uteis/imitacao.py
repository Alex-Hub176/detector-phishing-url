import json
from urllib.parse import urlparse


def imitacao(link):
    with open("dados/imitacao_marcas.json", "r") as arquivo:
        marcas = json.load(arquivo)
    
    with open("dados/palavras_perigosas.json", "r") as f:
        palavras_perigosas = json.load(f)


    site = urlparse(link).netloc.lower()
    caracteres_exemplo = ["1","0","@","3"]

    score = 0
    motivos = []
    for marca in marcas:
        if marca in site:
            score += 1    
            motivos.append(f"Marca suspeita [{marca}]")
            break  

    for categoria, palavras in palavras_perigosas.items():
        for p in palavras:
            if marca and p in site:
                score += 5
                motivos.append(f"Palavras suspeita [{p}] com a marca [{marca}]")

    for caracteres in caracteres_exemplo:
        if caracteres in site:
            score += 4
            motivos.append(f"Caractere Trocado [{caracteres}]")
            
    resultado = {
        "score":score,
        "motivos":motivos
    }

    return resultado




        
