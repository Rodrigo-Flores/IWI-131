def ganador(c1, c2, c3, meta):
    if int(c1) == int(meta):
        return 1

    elif int(c2) == int(meta):
        return 2

    elif int(c3) == int(meta):
        return 3

    else:
        return 0

def contar(palabra):
    count = 0
    for i in palabra:
        if i == 'a':
            count += 1

        elif i == 'e':
            count += 1

        elif i == 'i':
            count += 1

        elif i == 'o':
            count += 1

        elif i == 'u':
            count += 1

    return count

meta = int(input('Ingrese meta del Juego: '))

count_c1 = 0
count_c2 = 0
count_c3 = 0

flag = True
while flag:
    c1 = input('alianza 1: ')
    c2 = input('alianza 2: ')
    c3 = input('alianza 3: ')

    if (contar(c1) != contar(c2)) or (contar(c2) != contar(c3)) or (contar(c1) != contar(c3)):
        if (contar(c1) > contar(c2)) and (contar(c1) > contar(c3)):
            count_c1 += 1

        elif (contar(c2) > contar(c1)) and (contar(c2) > contar(c3)):
            count_c2 += 1

        elif (contar(c3) > contar(c1)) and (contar(c3) > contar(c2)):
            count_c3 += 1

    win = ganador(count_c1, count_c2, count_c3, meta)

    if win != 0:
        flag = False

print('La alianza gandora es:', win)
