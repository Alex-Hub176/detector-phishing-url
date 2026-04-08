# 🛡️ Analisador de Domínios & Detector de Phishing

Ferramenta desenvolvida em Python para analisar URLs e mensagens suspeitas, identificando possíveis ameaças como phishing, fraudes e sites maliciosos — com sistema de pontuação de risco.

---

## ⚙️ Funcionalidades

Através da biblioteca `urllib.parse`, ele desmonta a URL e realiza verificações em camadas:

1. **Detecção de Encurtadores (`encurtador`):** Verifica se o link tenta esconder o destino real usando serviços como *bit.ly*, *tinyurl*, *t.ly*, etc.

2. **Análise de Extensões Suspeitas (`extencoes_suspeitas`):** Checa se o domínio usa TLDs baratos ou gratuitos frequentemente associados a crimes cibernéticos (ex: `.xyz`, `.tk`, `.pw`).

3. **Filtro de Palavras Perigosas no Domínio (`palavras_dominio`):** Verifica se o domínio contém termos comumente usados para enganar usuários (ex: `promocao`, `gratis`, `banco`, `pix`), classificando a ameaça por categoria.

4. **Detecção de Imitação de Marcas (`imitacao`):** Identifica se o domínio tenta se passar por marcas conhecidas como Nubank, Bradesco, Correios, Amazon, entre outras — inclusive com detecção de caracteres trocados (ex: `@`, `0`, `1`).

5. **Detector de Palavras Suspeitas em Mensagens (`palavras_suspeitas`):** Analisa o texto de mensagens em busca de gatilhos de urgência, medo, promessas financeiras e pedidos de acesso a contas.

---

## 🎯 Sistema de Pontuação

Cada verificação contribui com pontos ao score final. O resultado é classificado em quatro níveis:

| Score | Classificação |
|-------|--------------|
| 0 – 2 | ✅ Seguro |
| 3 – 5 | ⚠️ Suspeito |
| 6 – 9 | 🔶 Alto Risco |
| 10+   | 🚨 Phishing |

---

## 🗂️ Estrutura do Projeto

```
├── Main.py                    # Ponto de entrada
├── verificador_geral.py       # Agrega todos os verificadores
├── uteis/
│   ├── __init__.py
│   ├── interface.py           # Menu e formatação de saída
│   ├── encurtador.py
│   ├── extencoes_suspeitas.py
│   ├── imitacao.py
│   ├── palavras_dominio.py
│   └── palavras_suspeitas.py
└── dados/
    ├── encurtadores.json
    ├── imitacao_marcas.json
    ├── palavras_perigosas.json
    └── palavras_chaves.json
```

---

## ▶️ Como usar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/detector-phishing.git
cd detector-phishing

# Execute
python Main.py
```

Sem dependências externas — usa apenas a biblioteca padrão do Python.

---

## 📦 Exemplo de saída

```
----------------------------------------
           DETECTOR DE GOLPE
----------------------------------------

Mensagem: Seu CPF foi bloqueado! Clique agora para regularizar
Site suspeito: http://bradesco-seguro.xyz/login

----------------------------------------
[URL]: bradesco-seguro.xyz
[Resultado]: Phishing
[Score]: 11
[Motivos]:
  Extenção suspeita [.xyz]
  Marca suspeita [bradesco]
  Palavra suspeita [login] com a marca [bradesco]
  Item suspeito [bloqueado] da categoria [urgencia]
```

---

## 🗺️ Roadmap

- [ ] Exportar resultados em JSON/CSV
- [ ] Suporte a análise em lote (múltiplos links de uma vez)
- [ ] Ampliar base de dados de encurtadores e marcas
- [ ] Interface web simples com Flask ou FastAPI

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor
Alex S.