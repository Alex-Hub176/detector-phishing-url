from urllib.parse import urlparse
import json


def palavras_perigosas(link):
    
    with open("dados/palavras_perigosas.json", "r") as f:
        palavras_perigosas = json.load(f)

    site_suspeito = urlparse(link).netloc

    for categoria, palavras in palavras_perigosas.items():
        for palavra in palavras:
            if palavra in site_suspeito:
                return 2    


