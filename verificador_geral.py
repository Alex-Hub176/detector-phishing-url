import uteis


def contador(link=''):
    score = [
    
        uteis.encurtador.encurtador(link),
        uteis.extencoes_suspeitas.extencoes_suspeitas(link),
        uteis.imitacao.imitacao(link),
        uteis.palavras_dominio.palavras_perigosas(link),
        uteis.palavras_suspeitas.detector_palavras(link)
        
        ]

    score_total = 0
    resultado = []
    for total in score:
        score_total += total["score"]
        resultado.extend(total["motivos"])
    resultado.append(score_total)

    return resultado






