# frase = input("Ingrese texto: ")
# significado = input("Ingrese significado: ")

frase = "Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<"
significado = "<3*corazon$:-D*cara feliz$>.<*incomodo$"

i = 0

a = 0

def extraccion():
    if significado[i] == "*":
        emoji = significado[:i]
        t = i + 1

    elif significado[i] == "$":
        significado_emoji = significado[t:i].upper()
        significado = significado[i+1:]    
        
    i+=1

    





"""
Ingrese texto: Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<
Ingrese significados:<3*corazon$:-D*cara feliz$>.<*incomodo$
Texto traducido: Hola CORAZON, cómo estás? CARA FELIZ. Voy atrasado a
la clase INCOMODO
"""