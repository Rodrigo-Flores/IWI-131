numero_1 = int(input("Ingrese un número: "))
numero_2 = int(input("Ingrese otro número: "))

final = True

total = 0

while final:
    resultado_1 = numero_1 // 2

    if resultado_1 % 2 != 0:
        total += numero_2
        numero_2 *= 2

    elif resultado_1 == 1:
        final = False

print("Total:", total)