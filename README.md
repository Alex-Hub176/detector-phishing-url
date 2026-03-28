# 🛡️ Analisador de Domínios & Detector de Phishing

Este projeto é uma ferramenta desenvolvida em Python para analisar URLs e identificar possíveis ameaças, como links de phishing, fraudes ou sites maliciosos. 

## ⚙️ Funcionalidades (Features)

Através da biblioteca `urllib.parse`, a ferramenta desmonta a URL e realiza três verificações principais:
1. **Detecção de Encurtadores (`encurtador`):** Verifica se o link tenta esconder o destino real usando serviços como *bit.ly*, *tinyurl*, etc.

2. **Análise de Extensões Suspeitas (`extencoes_suspeitas`):** Checa se o domínio usa TLDs baratos ou gratuitos frequentemente associados a crimes cibernéticos (ex: `.xyz`, `.tk`, `.pw`).

3. **Filtro de Palavras Perigosas (`palavras_perigosas`):** Lê um arquivo `palavras_perigosas.json` e verifica se o domínio contém termos comumente usados para enganar usuários (ex: "promocao", "gratis", "banco", etc.), classificando a ameaça por categoria.

## Ainda em desenvolvimento...