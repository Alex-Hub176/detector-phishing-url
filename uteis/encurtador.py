from urllib.parse import urlparse
import json

def encurtador(link):

    with open("dados/encurtadores.json","r") as f:
        encurtadores = json.load(f)

    suspeito = urlparse(link).netloc.lower()

    score = 0
    motivos = []

    for encurtador in encurtadores:
        if suspeito.endswith(encurtador):
            score = 2
            motivos.append(f"Uso de encurtador [{encurtador}]")
        
    
    resultado = {
        "score":score,
        "motivos":motivos
    }

    return resultado