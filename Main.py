import uteis
import verificador_geral
from urllib.parse import urlparse

uteis.interface.menu()
mensagem  = str(input("Mensagem: ")).strip().lower()
site = str(input("Site suspeito: ")).strip().lower()

url = urlparse(site).netloc.lower()


resultado = verificador_geral.contador(site,mensagem)
score = resultado[-1]
motivos = resultado[:-1]
uteis.interface.linha()

if score <=2:
    nivel = "Seguro"
elif score >= 3 and score <= 5:
    nivel = "Suspeito"
elif score >= 6 and score <= 9:
    nivel = "Alto risco"
elif score >= 10:
    nivel = "Phishing"


    
print(f""" 
[URL]: {url}
[Resultado]: {nivel}
[Score]: {score}
[Motivos]: """)
for motivo in motivos:
    print(motivo)


