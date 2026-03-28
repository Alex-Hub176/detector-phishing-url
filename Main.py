import uteis

uteis.interface.menu()

link = str(input("Cole ou Digite o Link suspeito: ")).strip()

uteis.verificar_dominio.encurtador(link)
uteis.verificar_dominio.extencoes_suspeitas(link)
uteis.verificar_dominio.palavras_perigosas(link)
# mensagem = str(input("Cole ou Digite a Mensagem suspeita: ")).strip()

# uteis.palavras_suspeitas.detector_palavras(mensagem)
    
    
# match escolha:
#     case 1:
#         uteis.verificar_dominio.encurtador("https://notebooklm.google.com/notebook/444a5e69-367e-496a-a620-ca167dae63e5")

#     case 2:
#         mensagem = str(input("Digite ou cole a mensagem suspeita: ")).lower()
#         uteis.palavras_suspeitas.detector_palavras(mensagem)

