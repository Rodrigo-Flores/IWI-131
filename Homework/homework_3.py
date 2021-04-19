"""

Autor: Rodrigo Flores
Carrera: Ingenieria Civil Informatica
Curso: IWI131

Observacion (1):
    Este codigo no posee ninguna tilde, y el lo posible nigun caracter fuera del alfabeto anglosajon.
    Asi se evitan errores innecesarios. 

Obervacion (2):
    Ciertamente pude haber utilizado funciones o clases para que el codigo quedara menos engorroso de ver.
    Pero no hemos pasado aun esa materia, asi que me abstengo.

"""

# --- Inicio del programa --- #

# Recolectando datos principales. Tales como:
valor_propiedad = float(input("Valor propiedad en UF (1500-13000: ")) # Valor de la propiedad
pie_porcentaje = int(input("Ingrese '%' del pie (20'%'-45'%')")) # Pie dado al banco
plazo = int(input("Ingrese Plazo (20, 25, 30: ")) # Plazo para pagar
tipo_vivienda = int(input("Tipo vivienda Casa(1) o Departamento(2): ")) # Tipo de vivienda de que se va a comprar
estado_vivienda = int(input("Estado vivienda Nueva(1) o Usada(2): ")) # Estado de la vivienda que se va a comprar

# Convirtiendo datos de usuario a datos utilizables
pie = pie_porcentaje/100

# Inicio de condicionales. Explicacion al extremo derecho de cada uno:
if tipo_vivienda == 1: # Casa
    if estado_vivienda == 1: # Nueva
        if plazo == 20: # 20 años
            pass
        elif plazo == 25: # 25 años
            pass

        elif plazo == 30: # 30 años
            pass

        else: # Error plazo
            print("Plazo invalido")
    elif estado_vivienda == 2: # Usada
        if plazo == 20: # 20 años
            pass
        elif plazo == 25: # 25 años
            pass

        elif plazo == 30: # 30 años
            pass

        else: # Error plazo
            print("Plazo invalido")

    else: # Error estado vivienda
        print("Estado vivienda invalido")

elif tipo_vivienda == 2: # Departamento
    if estado_vivienda == 1: # Nueva
        if plazo == 20: # 20 años
            pass
        elif plazo == 25: # 25 años
            pass

        elif plazo == 30: # 30 años
            pass

        else: # Error plazo
            print("Plazo invalido")

    elif estado_vivienda == 2: # Usada
        if plazo == 20: # 20 años
            pass
        elif plazo == 25: # 25 años
            pass

        elif plazo == 30: # 30 años
            pass

        else: # Error plazo
            print("Plazo invalido")

    else: # Error estado vivienda
        print("Estado vivienda invalido")

else: # Error tipo vivienda
    print("Tipo vivienda invalido")



# total_credito = VALUE
# dividendo_mensual = VALUE



