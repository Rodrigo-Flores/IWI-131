total_numeros = 0
pares = 0
impares = 0

flag_out = True
while flag_out:
    i = 1
    n = 0
    total = 0

    number = input("Ingrese cadena binaria: ")

    if len(number) < 4 or len(number) > 8:
        flag_out = False

    for j in number:
        if j != '1' and j != '0':
            flag_out = False

    if flag_out:
        while i <= len(number):
            if number[-i] == "1":
                total += 2**n

            n+=1
            i+=1

        print(total)


        total_numeros+=1
        if (total%2) == 0:
            pares+=1

        elif (total%2) != 0:
            impares+=1

print("total", total_numeros)
print("pares", pares)
print("impares", impares)