def linha(tamanho=40):
    print("-" * tamanho)


def menu():
    linha()
    print("DETECTOR DE GOLPE".center(40))
    linha()
    print("""
    1 - Analisar Link.
    2 - Detectar palavras suspeitas. 
          """)
    linha()