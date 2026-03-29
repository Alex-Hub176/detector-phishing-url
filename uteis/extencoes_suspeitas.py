from urllib.parse import urlparse
import json


def extencoes_suspeitas(link):

    dominios = [".xyz", ".gratis", ".top", ".click",".pw",".tk"]
    site_suspeito = urlparse(link).netloc

    for dominio in dominios:
        if dominio in site_suspeito:
            return 3

