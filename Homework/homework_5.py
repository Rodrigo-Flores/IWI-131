"""

Autor: Rodrigo Flores
Carrera: Ingenieria Civil Informatica
Curso: IWI131

Observacion (1):
    Este codigo no posee, en lo posible, ninguna tilde ni caracter fuera del alfabeto anglosajon.
    Asi se evitan errores innecesarios.

Recomendacion (1):
    Ejecutar desde una terminal.

"""

# Para determianr la Media Aritmetica
def media_aritmetica(n1, n2, n3):
    nf = (n1 + n2 + n3)/3 # Formula de Media Geometrica

    return nf

# Para determinar la Media Geometrica
def media_geometrica(n1, n2, n3):
    nf = (n1 * n2 * n3)**(1/3) # Formula de Media Geometrica

    return nf

# Para determianr la Media Vuelta
def media_vuelta(n1, n2, n3):
    nf = (n3 * ((media_aritmetica(n1, n2, n3)**2)))**(1/3) # Formula de Media Vuelta

    return nf

# Para determinar con que formula se aprueba el ramo
def aprueba(nf_aritmetica, nf_geometrica, nf_vuelta):
    if nf_aritmetica >= 55: # Si es True, aprueba con Media Aritmetica
        return 1

    elif nf_geometrica >= 55: # Si es True, aprueba con Media Geometrica
        return 2

    elif nf_vuelta >= 55: # Si es True, aprueba con Media Vuelta
        return 3

    else: # Si no es ninguno de lo anterior, entonces reprueba
        return 0

pedir_notas = True # Se inicializa la bandera del bucle

# Bucle principal
while pedir_notas:
    ramo = input("Ingrese el nombre del ramo: ") # Se solicita el nombre del ramo

    if ramo == "salir": # Si el usuario introduce "salir", termina el programa
        pedir_notas = False # La bandera se torna False
        print("Fin del programa - Desarrollado por Kiwi :D!") # Imprime mensaje final del programa

    else:
        n1 = int(input("Ingrese la 1era nota: ")) # Se solicita nota 1
        n2 = int(input("Ingrese la 2era nota: ")) # Se solicita nota 2
        n3 = int(input("Ingrese la 3era nota: ")) # Se solicita nota 3

        nf_aritmetica = int(round(media_aritmetica(n1, n2, n3), 0)) # Valor de la nota final segun Media Aritmetica
        nf_geometrica = int(round(media_geometrica(n1, n2, n3), 0)) # Valor de la nota final segun Media Geoemtrica
        nf_vuelta = int(round(media_vuelta(n1, n2, n3), 0)) # Valor de la nota final segun Media Vuelta

        print("Su nota final según la Media Aritmética es:", nf_aritmetica) # Se imprime la nota final de Media Aritmetica
        print("Su nota final según la Media Geométrica es:", nf_geometrica) # Se imprime la nota final de Media Geometrica
        print("Su nota final según la Media Vuelta es:", nf_vuelta) # Se imprime la nota final de Media Vuelta

        nf_aprobacion = aprueba(nf_aritmetica, nf_geometrica, nf_vuelta) # Valor de nota mayor, o en caso contrario, la de repruebo

        if nf_aprobacion == 0: # Reprueba
            print("Lamentablemente no puedes aprobar con ninguna de las fórmulas :'c")
            
        elif nf_aprobacion == 1: # Con la Media Aritmetica basta
            print("Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas", ramo, ":D") # Imprime en pantalla

        elif nf_aprobacion == 2: # Con la Media Geometrica basta
            print("Si la NF del ramo se calcula usando la Media Geométrica, entonces apruebas", ramo, ":D") # Imprime en pantalla

        elif nf_aprobacion == 3: # Con la Media Vuelta basta
            print("Si la NF del ramo se calcula usando la Media Vuelta, entonces apruebas", ramo, ":D") # Imprime en pantalla
