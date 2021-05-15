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

frase = input("Ingrese texto: ")
significado = input("Ingrese significado: ")

i = 0
anterior = 0
emoji = ""
significado_e = ""

'''
Ingrese texto: Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<
Ingrese significados:<3*corazon$:-D*cara feliz$>.<*incomodo$
'''



# Ciclo principal
while i < len(significado):
    if significado[i] == "$": # Extrayendo un emoji, junto a su significado
        actual = i # Guardando la variable i para que a la siguiente vuelta, no se inicie desde el principio

        substring = significado[anterior:actual] # Se extrae el emoji con el significado

        j = 0 # Se inicializa el contador para el bucle

        while j < len(substring): # Bucle para separar el emoji de su significado
            if substring[j] == "*": # Cuando la iteracion encuentre el asterisco, los separara
                emoji = substring[:j] # # Se extrae el emoji
                significado_e = substring[j+1:] # Se extrae el significado del emoji

            j += 1 # Se aumenta en uno para seguir iterando en el string

        
        anterior = actual + 1 # Ahora le sumamos el punto de corte del ultimo signo '$' + 1, 
                              # para partir desde el siguiente significado, sin incluir el signo '$'

        h = 0 # Se inicializa el contador para el bucle 
        nuevo = "" # Se crea una varible de string vacio, para contatenar la nueva frase

        while h < len(frase): # Bucle para insertar significado en la frase principal
            if emoji == frase[h:h+len(emoji)]: # Si emoji es igual a lo que se encuentra en el tramo seleccionado (que posee el mismo largo del emoji),
                                               # entonces, habra encontrado su equivalencia y ejecuta lo siguiente:
                nuevo += significado_e.upper() # Se añade el significado en mayuscula al string de concatenacion
                h += len(emoji) # Ya no nos sirve mas el tramo del emoji, avanzamos directamente la cantidad de caracteres, segun el largo del emoji

            else: # Si no
                nuevo += frase[h] # Le vamos añadiendo el resto de la frase, pues eso no es un emoji y no debe ser alterado

                h += 1 # Se incrementa el contador en 1 para iterar correctamente dentro de la frase principal

        frase = nuevo # Se guarda el valor de la frase, porque si no se hace, se va a perder el valor y solo se reemplazara uno

    i += 1 # Se incrementa el contador del bucle principal para iterar en el significado

print("Texto traducido:", frase) # Finalmente, se imprime en pantalla la frase traducidacd 

# Fin del programa


'''
CASOS DE PRUEBA

CASO 1:
    Ingrese texto: este es un [<>] de [ ! ] :D
    Ingrese significado: [<>]*mensaje$[ ! ]*prueba$:D*felicidad$
    Texto traducido: este es un MENSAJE de PRUEBA FELICIDAD

CASO 2:
    Ingrese texto: ME FUE RE [ok] EN EL X(
    Ingrese significado: [ok]*bien$X(*certamen$
    Texto traducido: ME FUE RE BIEN EN EL CERTAMEN

CASO 3:
    Ingrese texto: Un año más y puedo votar
    Ingrese significado: ñ*invalido$á*invalido$
    Texto traducido: Un aINVALIDOo mINVALIDOs y puedo votar

'''

