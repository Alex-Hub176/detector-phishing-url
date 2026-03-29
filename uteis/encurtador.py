from urllib.parse import urlparse
import json

def encurtador(link):

    with open("dados/encurtadores.json","r") as f:
        encurtadores = json.load(f)

    suspeito = urlparse(link).netloc.lower()

    for encurtador in encurtadores:
        if suspeito.endswith(encurtador):
            return 2