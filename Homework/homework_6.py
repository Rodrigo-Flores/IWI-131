# frase = input("Ingrese texto: ")
# significado = input("Ingrese significado: ")

frase = "Hola <3, cómo estás? :-D. Voy atrasado a la clase >.<"
significado = "<3*corazon$:-D*cara feliz$>.<*incomodo$"

significado_2 = significado

i = 0

while i < len(significado):
    if significado_2[i] == "*":
        emoji = significado_2[:i]
        t = i + 1

    elif significado_2[i] == "$":
        significado_emoji = significado_2[t:i].upper()
        significado_2 = significado_2[(i+2):]    

        traduccion = frase.replace(emoji, significado_emoji)  
        print(traduccion)

    i+=1

    

print(traduccion)