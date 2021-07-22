def tiene_restriccion(registro, patente, dia):
    no_catalitico_lunes = ["0","1","2","3"]
    no_catalitico_miercoles = ["4","5","6"]
    no_catalitico_viernes = ["7","8","9"]

    if " " in patente:
        separado = patente.split(" ")
        patente_letra = separado[0]
        patente_numero = separado[1]

    if "-" in patente:
        separado = patente.split("-")
        patente_letra = separado[0]
        patente_numero = separado[1]

    for i in registro:
        if i[-1] and patente == i[0]:
            if (dia.upper() == "LUNES") and (patente_letra[-1] < "G"):
                return True

            elif (dia.upper() == "MIERCOLES" or dia.upper() == "MIÉRCOLES") and (patente_letra[-1] >= "G" and patente_letra[-1] <= "N"):
                return True

            elif (dia.upper() == "VIERNES") and (patente_letra[-1] > "N"):
                return True

            else:
                return False

        elif i[-1] == False and patente == i[0]:
            if (dia.upper() == "LUNES") and (patente_numero[-1] in no_catalitico_lunes):
                return True

            elif (dia.upper() == "MIERCOLES" or dia.upper() == "MIÉRCOLES") and (patente_numero[-1] in no_catalitico_miercoles):
                return True

            elif (dia.upper() == "VIERNES") and (patente_numero[-1] in no_catalitico_viernes):
                return True

            else:
                return False

def restringidos(registro, dia):
    
    lst = []

    for patente, ciudad, nombre, catalitico in registro:
        if tiene_restriccion(registro, patente, dia):
            lst.append((ciudad, patente))

    lst.sort()
    lst.reverse()

    return lst

registro = [
("CRTJ 32", "Valpyraiso", "Juan Perez", True),
("RX-2134", "Sanpyago", "Ana Martinez", False),
("ADNT 28", "Pyna del Mar", "Fernanda Jara", False),
("ZZ-9999", "Pyca", "Pedro Allende", True),
("AK-2130", "Sanpyago", "Paloma Blanco", True),
("ABCD 19", "Copymbo", "Ana Roa", False)]

print(restringidos(registro, "MIERCOLES"))
print(restringidos(registro, "LUNES"))