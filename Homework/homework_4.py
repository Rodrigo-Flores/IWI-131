"""

Autor: Rodrigo Flores
Carrera: Ingenieria Civil Informatica
Curso: IWI131

Observacion (1):
    Este codigo no posee ninguna tilde, y el lo posible nigun caracter fuera del alfabeto anglosajon.
    Asi se evitan errores innecesarios.

Observacion (2):
    Funciona tanto en Linux como en Windows.

Recomendacion (1):
    Ejecutar desde una terminal.

"""

## Sucursales y acumulacciones
sucursal_1 = 0 # S1
sucursal_2 = 0 # S2
sucursal_3 = 0 # S3S

## Sucursales y sus respectivas coordenadas
# Coordenadas nombre de sucursal_2
nombre_sucursal_1 = input("Nombre sucursal 1: ")
x_sucursal_1 = int(input("Coordenada x: "))
y_sucursal_1 = int(input("Coordenada y: "))

# Coordenadas y nombre de sucursal 2
nombre_sucursal_2 = input("Nombre sucursal 2: ")
x_sucursal_2 = int(input("Coordenada x: "))
y_sucursal_2 = int(input("Coordenada y: "))

# Coordenadas y nombre de sucursal 3
nombre_sucursal_3 = input("Nombre sucursal 3: ")
x_sucursal_3 = int(input("Coordenada x: "))
y_sucursal_3 = int(input("Coordenada y: "))

print() # Salto de linea

## Platos y totales
carnivoro = 4000 # Plato 1
vegetariano = 3000 # Plato 2
vegano = 3500 # Plato 3
total_pedido = 0
total_recaudado = 0

## Inicializando valores booleanos para las condiciones de los bucles de tipo "while"
flag_menor = True
flag_in = True
flag_out = True

## Loop principal
while flag_out:
    # Volvemos a su estado base las variables
    flag_in = True
    total_pedido = 0
    flag_menor = True
  
    # Loop para elegir plato
    while flag_in:
        pedido = input("Ingrese numero del plato: ")

        if pedido == "1": # Plato 1
            total_pedido += carnivoro

        elif pedido == "2": # Plato 2
            total_pedido += vegetariano

        elif pedido == "3": # Plato 3
            total_pedido += vegano

        elif pedido == "-1": # Dejar de pedir platos
            flag_in = False

            print("Total del pedido $", total_pedido)

    # Solicitando coordenada al cliente (x, y)
    coordenada_x = float(input("Ingrese coordenada x cliente: "))
    coordenada_y = float(input("Ingrese coordenada y cliente: "))

    # Calculando distancia entre dos puntos del plano
    distancia_cliente_a_S1 = ((x_sucursal_1-coordenada_x)**2 + (y_sucursal_1-coordenada_y)**2)**1/2 # Sucursal 1
    distancia_cliente_a_S2 = ((x_sucursal_2-coordenada_x)**2 + (y_sucursal_2-coordenada_y)**2)**1/2 # Sucursal 2
    distancia_cliente_a_S3 = ((x_sucursal_3-coordenada_x)**2 + (y_sucursal_3-coordenada_y)**2)**1/2 # Sucursal 3
    
    # Loop para ver la mejor ubicacion para realizar la entrega
    while flag_menor:
        # Sucursal 1 es la mejor distancias hasta el cliente
        if distancia_cliente_a_S1 < distancia_cliente_a_S2 and distancia_cliente_a_S1 < distancia_cliente_a_S3: # Evaluando menor distancia
            menor_distancia = distancia_cliente_a_S1 # Eligiendo nueva menor distancia
            sucursal_1 += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por", nombre_sucursal_1)
            flag_menor = False # Cerrando el bucle con flag_menor como False

        # Sucursal 2 es la mejor distancias hasta el cliente
        elif distancia_cliente_a_S2 < distancia_cliente_a_S1 and distancia_cliente_a_S2 < distancia_cliente_a_S3: # Evaluando menor distancia
            menor_distancia = distancia_cliente_a_S2 # Eligiendo nueva menor distancia
            sucursal_2 += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por", nombre_sucursal_2)
            flag_menor = False # Cerrando el bucle con flag_menor como False

        # Sucursal 3 es la mejor distancias hasta el cliente
        elif distancia_cliente_a_S3 < distancia_cliente_a_S1 and distancia_cliente_a_S3 < distancia_cliente_a_S2: # Evaluando menor distancia
            menor_distancia = distancia_cliente_a_S3 # Eligiendo nueva menor distancia
            sucursal_3 += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por", nombre_sucursal_3)
            flag_menor = False # Cerrando el bucle con flag_menor como False

    total_recaudado += total_pedido

    continuar = input("¿Desea registrar otro pedido?: ")
    print() # Salto de linea

    if continuar == "si" or continuar == "SI" or continuar == "Si" or continuar == "sI":
        pass # Pasa sin realizar cambios que afecten a la continuidad del bucle

    else:
        flag_out = False # Cerrando el bucle con flag_menor como False

## Imprimiendo en pantalla los datos solicitados
print("#####  Estadísticas Finales #####") # Titulo
print("Monto total recaudado $", total_recaudado) # Total de dinero
print(nombre_sucursal_1,"entregó", sucursal_1,"pedidos") # Total sucursal_1
print(nombre_sucursal_2,"entregó", sucursal_2,"pedidos") # Total sucursal_2
print(nombre_sucursal_3,"entregó", sucursal_3,"pedidos") # Total sucursal_3

## Fin del programa

"""
@CASOS DE PRUEBA

# -- Caso 1 -- #
Nombre sucursal 1: Tera
Coordenada x: 1
Coordenada y: -6
Nombre sucursal 2: Giga
Coordenada x: 8
Coordenada y: 0
Nombre sucursal 3: Peta
Coordenada x: 5
Coordenada y: -5

Ingrese numero del plato: 1
Ingrese numero del plato: 1
Ingrese numero del plato: 1
Ingrese numero del plato: 1
Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido $ 20000
Ingrese coordenada x cliente: 5
Ingrese coordenada y cliente: 5
Su pedido sera entregado por Giga
¿Desea registrar otro pedido?: si

Ingrese numero del plato: 2
Ingrese numero del plato: 2
Ingrese numero del plato: 2
Ingrese numero del plato: -1
Total del pedido $ 9000
Ingrese coordenada x cliente: 3
Ingrese coordenada y cliente: -3
Su pedido sera entregado por Peta
¿Desea registrar otro pedido?: no

#####  Estadísticas Finales #####
Monto total recaudado $ 29000
Tera entregó 0 pedidos
Giga entregó 1 pedidos
Peta entregó 1 pedidos

# -- Caso 2 -- #
Nombre sucursal 1: Nano
Coordenada x: 1
Coordenada y: 1
Nombre sucursal 2: Micro 
Coordenada x: -1
Coordenada y: 5
Nombre sucursal 3: Pico
Coordenada x: 4
Coordenada y: -6

Ingrese numero del plato: 3
Ingrese numero del plato: 3
Ingrese numero del plato: 3
Ingrese numero del plato: 3
Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido $ 18000
Ingrese coordenada x cliente: 2
Ingrese coordenada y cliente: -9
Su pedido sera entregado por Pico
¿Desea registrar otro pedido?: si

Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido $ 4000
Ingrese coordenada x cliente: 0
Ingrese coordenada y cliente: 0
Su pedido sera entregado por Nano
¿Desea registrar otro pedido?: no

#####  Estadísticas Finales #####
Monto total recaudado $ 22000
Nano entregó 1 pedidos
Micro entregó 0 pedidos
Pico entregó 1 pedidos

# -- Caso 3 -- #
Nombre sucursal 1: Sol   
Coordenada x: 0
Coordenada y: 0
Nombre sucursal 2: Betelgeuse
Coordenada x: 10
Coordenada y: -1
Nombre sucursal 3: Sagitario A
Coordenada x: -10 
Coordenada y: -20

Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido $ 4000
Ingrese coordenada x cliente: -10
Ingrese coordenada y cliente: -10
Su pedido sera entregado por Sagitario A
¿Desea registrar otro pedido?: si

Ingrese numero del plato: 2
Ingrese numero del plato: 1
Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido $ 11000
Ingrese coordenada x cliente: 1
Ingrese coordenada y cliente: 1
Su pedido sera entregado por Sol
¿Desea registrar otro pedido?: si

Ingrese numero del plato: 2
Ingrese numero del plato: 2
Ingrese numero del plato: 2
Ingrese numero del plato: -1
Total del pedido $ 9000
Ingrese coordenada x cliente: 15
Ingrese coordenada y cliente: -5
Su pedido sera entregado por Betelgeuse
¿Desea registrar otro pedido?: no

#####  Estadísticas Finales #####
Monto total recaudado $ 24000
Sol entregó 1 pedidos
Betelgeuse entregó 1 pedidos
Sagitario A entregó 1 pedidos

"""