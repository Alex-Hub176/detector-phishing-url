import json
from urllib.parse import urlparse


def imitacao(link):
    with open("dados/imitacao_marcas.json", "r") as arquivo:
        marcas = json.load(arquivo)
    
    with open("dados/palavras_perigosas.json", "r") as f:
        palavras_perigosas = json.load(f)


    site = urlparse(link).netloc.lower()
    caracteres_exemplo = ["1","0","@","3"]

    marca = None
    score = 0
    motivos = []
    for m in marcas:
        if m in site:
            marca = m
            score += 1    
            motivos.append(f"Marca suspeita [{marca}]")
            break  

    for categoria, palavras in palavras_perigosas.items():
        for palavra in palavras:
            if marca is not None and palavra in site:
                score += 5
                motivos.append(f"Palavras suspeita [{palavra}] com a marca [{marca}]")

    for caracteres in caracteres_exemplo:
        if caracteres in site:
            score += 4
            motivos.append(f"Caractere Trocado [{caracteres}]")
            
    resultado = {
        "score":score,
        "motivos":motivos
    }

    return resultado




        
