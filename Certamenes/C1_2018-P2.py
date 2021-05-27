par = 0
impar = 0
total = 0
bytes = 0
binary = True
while binary:
    up = 7
    total = 0

    while up >= 0:
        num = int(input())

        if num == 1:
            total += (2**up)

        up -= 1

    if total == 0:
        binary = False

    if binary != False:
        if (total%2) == 0:
            par += 1

        elif (total%2) != 0:
            impar += 1

        bytes += 1

    print("Numero:",total)

print("Bytes calculados:",bytes)
print("Pares calculados:",par)
print("Impares calculados:",impar)