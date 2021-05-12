# frase = input("Ingrese texto: ")
# significado = input("Ingrese significado: ")

frase = "Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<"
significado = "<3*corazon$:-D*cara feliz$>.<*incomodo$"
nuevo_significado = significado

i = 0
traduccion = ""

def extraccion():
    nuevo_significado = significado
    while True:
        if nuevo_significado[i] == "*":
            emoji = nuevo_significado[:i]
            t = i + 1

        elif nuevo_significado[i] == "$":
            significado_emoji = nuevo_significado[t:i].upper()
            nuevo_significado = nuevo_significado[i+2:]
            break
            
        i+=1

    return emoji, significado_emoji,nuevo_significado

while len(nuevo_significado) < 5:
    emoji, significado_emoji,nuevo_significado = extraccion()

    traduccion = frase.replace(emoji, significado_emoji)

print(traduccion)

    





"""
Ingrese texto: Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<
Ingrese significados:<3*corazon$:-D*cara feliz$>.<*incomodo$
Texto traducido: Hola CORAZON, cómo estás? CARA FELIZ. Voy atrasado a
la clase INCOMODO
"""