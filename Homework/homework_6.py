# frase = input("Ingrese texto: ")
# significado = input("Ingrese significado: ")

frase = "Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<"
significado = "<3*corazon$:-D*cara feliz$>.<*incomodo$"
nuevo_significado = significado

<<<<<<< HEAD
significado_2 = significado

i = 0

while i < len(significado):
    if significado_2[i] == "*":
        emoji = significado_2[:i]
        t = i + 1

    elif significado_2[i] == "$":
        significado_emoji = significado_2[t:i].upper()
        significado_2 = significado_2[(i+2):]    
=======
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

    

>>>>>>> 1bbd3b313eb83a4b39de15320023a3af69ae37b6

        traduccion = frase.replace(emoji, significado_emoji)  
        print(traduccion)

    i+=1

    

print(traduccion)