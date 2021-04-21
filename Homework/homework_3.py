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

Recomendacion (1):
    Ejecutar desde una terminal.

"""

# --- Inicio del programa --- #

# Recolectando datos principales. Tales como:

valor_propiedad = float(input("Valor propiedad en UF (1500-13000): ")) # Valor de la propiedad
if valor_propiedad < 1500 or valor_propiedad > 13000: # Evaluando error
    print("Error: Valor fuera de rango")
    exit() # Terminando el programa

pie_porcentaje = float(input("Ingrese % del pie (20%-45%): ")) # Pie dado al banco
if pie_porcentaje < 20 or pie_porcentaje > 45: # Evaluando error
    print("Error: Pie fuera de rango") # Imprimir error
    exit() # Terminando el programa

plazo = int(input("Ingrese Plazo (20, 25, 30): ")) # Plazo para pagar
if plazo != 20 and plazo != 25 and plazo != 30: # Evaluando error
    print("Plazo invalido") # Imprimir error
    exit() # Terminando el programa

tipo_vivienda = int(input("Tipo vivienda Casa(1) o Departamento(2): ")) # Tipo de vivienda de que se va a comprar
if tipo_vivienda != 1 and tipo_vivienda != 2: # Evaluando error
    print("Tipo de vivienda invalido") # Imprimir error
    exit() # Terminando el programa

estado_vivienda = int(input("Estado vivienda Nueva(1) o Usada(2): ")) # Estado de la vivienda que se va a comprar
if estado_vivienda != 1 and estado_vivienda !=2: # Evaluando error
    print("Estado de vivienda invalido") # Imprimir error
    exit() # Terminando el programa

# Convirtiendo datos de usuario a datos utilizables
pie = pie_porcentaje/100

# Inicio de condicionales. Explicacion al extremo derecho de cada uno:

# --- CASA ---
if tipo_vivienda == 1:
    if estado_vivienda == 1: # NUEVO
        if plazo == 20: # 20 años
            # 20% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.2)
            nuevo_valor_propiedad += ((0.5 + 0.8) * 12 * 20)
            dividendo_mensual = nuevo_valor_propiedad / (20 * 12)

        elif plazo == 25: # 25 años
            # 30% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.3)
            nuevo_valor_propiedad += ((0.5 + 0.8) * 12 * 25)
            dividendo_mensual = nuevo_valor_propiedad / (25 * 12)

        elif plazo == 30: # 30 años
            # 35% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.35)
            nuevo_valor_propiedad += ((0.5 + 0.8) * 12 * 30)
            dividendo_mensual = nuevo_valor_propiedad / (30 * 12)

    elif estado_vivienda == 2: # USADO
        if plazo == 20: # 20 años
            # 22% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.22)
            nuevo_valor_propiedad += ((0.5) * 12 * 20)
            dividendo_mensual = nuevo_valor_propiedad / (20 * 12)

        elif plazo == 25: # 25 años
            # 27% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.27)
            nuevo_valor_propiedad += ((0.5) * 12 * 25)
            dividendo_mensual = nuevo_valor_propiedad / (25 * 12)

        elif plazo == 30: # 30 años
            # 31% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.31)
            nuevo_valor_propiedad += ((0.5) * 12 * 30)
            dividendo_mensual = nuevo_valor_propiedad / (30 * 12)

# --- DEPARTAMENTO ---
elif tipo_vivienda == 2:
    if estado_vivienda == 1: # NUEVA
        if plazo == 20: # 20 años
            # 28% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.28)
            nuevo_valor_propiedad += ((0.5 + 0.8 + 0.3) * 12 * 20)
            dividendo_mensual = nuevo_valor_propiedad / (20 * 12)

        elif plazo == 25: # 25 años
            # 33% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.33)
            nuevo_valor_propiedad += ((0.5 + 0.8 + 0.3) * 12 * 25)
            dividendo_mensual = nuevo_valor_propiedad / (25 * 12)

        elif plazo == 30: # 30 años
            # 41% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.41)
            nuevo_valor_propiedad += ((0.5 + 0.8 + 0.3) * 12 * 30)
            dividendo_mensual = nuevo_valor_propiedad / (30 * 12)

    elif estado_vivienda == 2: # USADA
        if plazo == 20: # 20 años
            # 26% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.26)
            nuevo_valor_propiedad += ((0.5 + 0.3) * 12 * 20)
            dividendo_mensual = nuevo_valor_propiedad / (20 * 12)

        elif plazo == 25: # 25 años
            # 32% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.32)
            nuevo_valor_propiedad += ((0.5 + 0.3) * 12 * 25)
            dividendo_mensual = nuevo_valor_propiedad / (25 * 12)

        elif plazo == 30: # 30 años
            # 37% de interes
            nuevo_valor_propiedad = valor_propiedad - (valor_propiedad * pie)
            nuevo_valor_propiedad += (nuevo_valor_propiedad * 0.37)
            nuevo_valor_propiedad += ((0.5 + 0.3) * 12 * 30)
            dividendo_mensual = nuevo_valor_propiedad / (30 * 12)

# Redondeando los valores a los 2 decimales pedidos
nuevo_valor_propiedad = round(nuevo_valor_propiedad, 2)
dividendo_mensual = round(dividendo_mensual, 2)

# Imprimiendo en pantalla la informacion solicitada
print("Total de credito a pagar", nuevo_valor_propiedad, "UF")
print("Dividendo mensual", dividendo_mensual, "UF")

# Fin del programa