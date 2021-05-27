num_init = input('Ingrese un número palindrómico: ')

count = 0
flag = True
while flag:
    if num_init != num_init[::-1]:
        num_init = str(int(num_init) + int(num_init[::-1]))

        if num_init != num_init[::-1]:
            print('Intermedio: ', num_init)

        count+=1

    else:
        flag = False

print('Generado en', count, 'pasos.')
print('Palíndromo final: ', num_init)



