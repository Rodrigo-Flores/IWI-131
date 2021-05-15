def divisores(num):
    div = 0
    i = 1
    while i <= num:
        if num%i == 0:
            div +=1
        i += 1
    if div == cant_divisores:
        return True
    return False

cont_alianza_1 = 0
cont_alianza_2 = 0
cont_alianza_3 = 0

cant_divisores = int(input("Cantidad de divisores: "))

alianza_1 = True
while alianza_1:
    numero_1 = int(input("Ingrese número:"))
    n_divisores = divisores(numero_1)
    if n_divisores:
        cont_alianza_1 +=1

    else:
        print("ALIANZA 1 :",cont_alianza_1, "correctas")
        alianza_1 = False

alianza_2 = True
while alianza_2:
    numero_2 = int(input("Ingrese número:"))
    n_divisores = divisores(numero_2)
    if n_divisores:
        cont_alianza_2 += 1

    else:
        print("ALIANZA 2 :", cont_alianza_2, "correctas")
        alianza_2 = False

alianza_3 = True
while alianza_3:
    numero_3 = int(input("Ingrese número:"))
    n_divisores = divisores(numero_3)
    if n_divisores:
        cont_alianza_1 += 1

    else:
        print("ALIANZA 3 :", cont_alianza_3, "correctas")
        alianza_3 = False

if (cont_alianza_1 > cont_alianza_2) and (cont_alianza_1 >cont_alianza_3):
    print("La alianza ganadora es la 1 con",cont_alianza_1, "correctas.")

elif (cont_alianza_2 > cont_alianza_1) and (cont_alianza_2 >cont_alianza_3):
    print("La alianza ganadora es la 2 con",cont_alianza_2, "correctas.")

elif (cont_alianza_3 > cont_alianza_2) and (cont_alianza_3 >cont_alianza_1):
    print("La alianza ganadora es la 3 con",cont_alianza_3, "correctas.")