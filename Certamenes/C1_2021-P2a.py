def votos_partido(votos, partido):
    i = 0
    n = 0
    votos += '$'
    cantidad_votos = 0
    while i < len(votos):
        if votos[i] == '$':
            sub = votos[n:i] # se saca un substring con el aprtido individual

            if sub == partido: # Si el substring es el partido que buscamos, sumamos un voto
                cantidad_votos+=1 

            n = i + 1

        i+=1

    return cantidad_votos