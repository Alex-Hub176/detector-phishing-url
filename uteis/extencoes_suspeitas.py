from urllib.parse import urlparse
import json


def extencoes_suspeitas(link):

    dominios = [".xyz", ".gratis", ".top", ".click",".pw",".tk"]
    site_suspeito = urlparse(link).netloc
    
    score = 0
    motivos = []

    for dominio in dominios:
        if dominio in site_suspeito:
            score = 3
            motivos.append(f"Extenção suspeita [{dominio}]")


    resultado = {
            "score":score,
            "motivos":motivos
            }
    
    return resultado
            
    

