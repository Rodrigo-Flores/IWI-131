def votos_partido(votos, partido):
    i = 0
    n = 0
    votos += '$'
    cantidad_votos = 0
    while i < len(votos):
        if votos[i] == '$':
            sub = votos[n:i]

            if sub == partido:
                cantidad_votos+=1

            n = i + 1
        i+=1

    return cantidad_votos


coaliciones = input('Ingrese coaliciones: ')
coaliciones+=';'
votos = input('Ingrese votos por partido: ')
votos+='$'

i = 0
n = 0
mayor = 0
while i < len(coaliciones):
    count = 0
    if coaliciones[i] == ';': # Se separan las coliciones
            sub = coaliciones[n:i]

            h = 0
            j = 0
            while h < len(sub): # Se separan las coaliciones de sus respectivos partidos
                if sub[h] == ':':
                    coal = sub[j:h] # Guardamos el nombre de la coalicion
                    partidos = sub[h+1:] # Guardamos los partidos
                    partidos+='-' # Modificamos el string para que opere bien

                    j = h + 1

                    a = 0
                    b = 0
                    print('Coalición:', coal)
                    while a < len(partidos): # Contaremos votos y eligeremos el mayor
                        if partidos[a] == '-':
                            partido_indi = partidos[b:a] # Separamos cad partido individualmente

                            voto_por_partido = votos_partido(votos, partido_indi) # Contamos votos
                            print(partido_indi, voto_por_partido)
                            count+=voto_por_partido

                            b = a + 1

                        a+=1

                        if a == len(partidos): # Elegimos el mayor
                            print('Total coalición', coal, ':',count)

                            if count > mayor:
                                mayor = count
                                name = coal

                h+=1

            n = i + 1
    
    i+=1

print('La coalición ganadora es', name, 'con', mayor, 'votos')
