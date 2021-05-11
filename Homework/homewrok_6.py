frase = input("Ingrese texto: ")
significado = input("Ingrese significado: ")


emoji = ""
traduccion = ""

for i in significado:
    if i == "*":
        emoji = significado[:i]
        temp = i +1

    elif i == "$":
        traduccion = significado[temp:i]

    for n in frase:
        if n == emoji:
            



'''
Ingrese texto: Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<
Ingrese significados:<3*corazon$:-D*cara feliz$>.<*incomodo$
Texto traducido: Hola CORAZON, cómo estás? CARA FELIZ. Voy atrasado a
la clase INCOMODO
'''