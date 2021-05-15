# Solicitando dos numero al usuario para multiplicarlos
a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

# Inicializando varible acumulativa para que no tenga un valor "basura"
suma = 0

# Inicializando la "bandera" para entrar al bucle, y luego terminarlo
flag = True

# Bucle principal
while flag:
    if (a%2) != 0: # Si el primero numero (a) es impar, se realiza la opracion
        suma += b
        b *= 2
        
    else: # Caso contrario, se multiplica el segundo numero por 2 de igual manera
        b *= 2

    if a == 1: # Si el nuevo valor del primer numero (a) es igual a 1, el programa finaliza con la condicion falsa
        flag = False

    a = a//2

# Se imprime en pantalla el resultado de la multiplicacion
print("Total:", suma)

# Fin del programa