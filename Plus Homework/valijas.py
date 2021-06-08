def descartar(lista):
    l = []
    for i in lista:
        if ((i[1][0])**2 + (i[1][1])**2)**(1/2) <= 30: 
            l.append(i)

    return l

def distancia(lista):
    d = ((i[1][0])**2 + (i[1][1])**2)**(1/2)

def ganancia(encomiendas, destinos):
    l = []
    for i in encomiendas:
        volumen = i[1][0] * i[1][1] * i[1][2]

        # ingresa = 0.1 * volumen * distancia



destinos = [
    [10234,[-4,15]],
    [36890,[2,4]],
    [34102,[18,-13]],
    [1, [1000,1000]]
]



# def viajes_a_realizar(encomiendas, destinos):
    # pass
