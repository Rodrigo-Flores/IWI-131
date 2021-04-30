a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

suma = 0
flag = True

while flag:
    if (a%2) != 0:
        suma += b
        b *= 2
        
    else:
        b *= 2

    if a == 1:
        flag = False

    a = a//2

print("Total:", suma)