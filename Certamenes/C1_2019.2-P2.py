import random

def mejor(votos):
    votos = str(votos)
    A = int(votos[0])
    B = int(votos[1])
    C = int(votos[2])
    D = int(votos[3])

    upper = 0

    if (A>=4) or (B>=4) or (C>=4) or (D>=4):
        if A > upper:
            upper = A
            song = 'A'


        if B > upper:
            upper = B
            song = 'B'

        if C > upper:
            upper = C
            song = 'C'

        if D > upper:
            upper = D
            song = 'D'

        return song

    else:
        return ''

count_A = 0
count_B = 0
count_C = 0
count_D = 0

for i in range(1000):
    vote = input('voto? ')

    fav = mejor(vote)

    if fav == 'A':
        count_A+=1

    elif fav == 'B':
        count_B+=1

    elif fav == 'C':
        count_C+=1

    elif fav == 'D':
        count_D+=1

upper = 0

if count_A > upper:
    upper = count_A
    best = 'A'

elif count_B > upper:
    upper = count_B
    best = 'B'

elif count_C > upper:
    upper = count_C
    best = 'C'

elif count_D > upper:
    upper = count_D
    best = 'D'

print('La favorita es', best,'con 510 votos.')