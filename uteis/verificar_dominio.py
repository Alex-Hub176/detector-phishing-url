from urllib.parse import urlparse
import json


def encurtador(link):

    encurtadores = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "cutt.ly"]
    suspeito = urlparse(link).netloc

    for encurtador in encurtadores:
        if encurtador in suspeito:
            print(f"Esse site está usando um encurtador {[encurtador]}")
        else:
            print(suspeito)
        break


def extencoes_suspeitas(link):

    dominios = [".xyz", ".gratis", ".top", ".click",".pw",".tk"]
    site_suspeito = urlparse(link).netloc

    for dominio in dominios:
        if dominio in site_suspeito:
            print(f"Esse site está usando uma extensão frequentemente associadas a crimes cibernéticos[{dominio}]")


def palavras_perigosas(link):
    
    with open("palavras_perigosas.json", "r") as f:
        palavras_perigosas = json.load(f)

    site_suspeito = urlparse(link).netloc
    encontradas = []

    for categoria, palavras in palavras_perigosas.items():
        for palavra in palavras:
            if palavra in site_suspeito:
                print(f"palavra suspeita {palavra},sua categoria {categoria}")


