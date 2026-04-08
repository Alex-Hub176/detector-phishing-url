def linha(tamanho=40):
    print("-" * tamanho)


def menu():
    linha()
    print("DETECTOR DE PHISHING-URL".center(40))
    linha()
    print("""
    ANÁLISE DE MENSAGEM E URL.
          1 - Digite ou cole a Mensagem, se não ouver Deixe em branco.
          2 - Digite ou cole o site suspeito.
          """)
    linha()