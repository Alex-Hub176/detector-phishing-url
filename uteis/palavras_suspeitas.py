import json

def detector_palavras(texto):
    with open("palavras_chaves.json", "r") as arquivo:
        palavras_chaves = json.load(arquivo)

    encontradas = []

    for categoria, lista_palavras in palavras_chaves.items():
        for palavras in lista_palavras:
            if palavras in texto:
                encontradas.append((palavras,categoria))
                
    if encontradas:
        for palavra, categorias in encontradas:
            print(f"[{palavra}] (categoria: {categorias})")
    else:
        print("Nenhuma palavra suspeita")

    
        


