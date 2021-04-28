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
san_joaco = 0 # SJ
vitacumbia = 0 # VC
dignidad = 0 # DG

## Sucursales y sus respectivas coordenadas
# Coordenadas de Vitacumbia
x_vitacumbia = 6
y_vitacumbia = -3

# Coordenadas de San joaco
x_san_joaco = -1
y_san_joaco = 5

# Coordenadas de Dignidad
x_dignidad = 0
y_dignidad = 0

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
    distancia_cliente_a_VC = ((x_vitacumbia-coordenada_x)**2 + (y_vitacumbia-coordenada_y)**2)**1/2 # Vitacumbia
    distancia_cliente_a_SJ = ((x_san_joaco-coordenada_x)**2 + (y_san_joaco-coordenada_y)**2)**1/2 # San Joaco
    distancia_cliente_a_DG = ((x_dignidad-coordenada_x)**2 + (y_dignidad-coordenada_y)**2)**1/2 # Dignidad
    
    # Loop para ver la mejor ubicacion para realizar la entrega
    while flag_menor:
        # Vitacumbia es la mejor distancias hasta el cliente
        if distancia_cliente_a_VC < distancia_cliente_a_SJ and distancia_cliente_a_VC < distancia_cliente_a_DG: # Evaluando menor distancia
            menor_distancia = distancia_cliente_a_VC # Eligiendo nueva menor distancia
            vitacumbia += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por Vitacumbia")
            flag_menor = False # Cerrando el bucle con flag_menor como False

        # San Joaco es la mejor distancias hasta el cliente
        elif distancia_cliente_a_SJ < distancia_cliente_a_VC and distancia_cliente_a_SJ < distancia_cliente_a_DG: # Evaluando menor distancia
            menor_distancia = distancia_cliente_a_SJ # Eligiendo nueva menor distancia
            san_joaco += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por San Joaco")
            flag_menor = False # Cerrando el bucle con flag_menor como False

        # Dignidad es la mejor distancias hasta el cliente
        elif distancia_cliente_a_DG < distancia_cliente_a_VC and distancia_cliente_a_DG < distancia_cliente_a_SJ: # Evaluando menor distancia
            menor_distancia = distancia_cliente_a_DG # Eligiendo nueva menor distancia
            dignidad += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por Dignidad")
            flag_menor = False # Cerrando el bucle con flag_menor como False

    total_recaudado += total_pedido

    continuar = input("¿Desea registrar otro pedido?: ")
    print()

    if continuar == "si" or continuar == "SI" or continuar == "Si" or continuar == "sI":
        pass # Pasa sin realizar cambios que afecten a la continuidad del bucle

    else:
        flag_out = False # Cerrando el bucle con flag_menor como False

## Imprimiendo en pantalla los datos solicitados
print("#####  Estadísticas Finales #####") # Titulo
print("Monto total recaudado $", total_recaudado) # Total de dinero
print("Vitacumbia entregó ", vitacumbia,"pedidos") # Total Vitacumbia
print("San Joaco entregó ", san_joaco, "pedidos") # Total San Joaco
print("Dignidad entrego", dignidad, "Pedidos") # Total Dignidad

## Fin del programa

"""
@CASOS DE PRUEBA

 # -- Caso : -- #
Ingrese numero del plato: 1
Ingrese numero del plato: 2
Ingrese numero del plato: 3
Ingrese numero del plato: -1
Total del pedido $ 10500
Ingrese coordenada x cliente: 5
Ingrese coordenada y cliente: 5
Su pedido sera entregado por San Joaco
¿Desea registrar otro pedido?: si

Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido $ 4000
Ingrese coordenada x cliente: 5
Ingrese coordenada y cliente: 5
Su pedido sera entregado por San Joaco
¿Desea registrar otro pedido?: no

#####  Estadísticas Finales #####
Monto total recaudado $ 14500
Vitacumbia entregó  0 pedidos
San Joaco entregó  2 pedidos
Dignidad entrego 0 Pedidos

# -- Caso 2 -- #
Ingrese numero del plato: 2
Ingrese numero del plato: 3
Ingrese numero del plato: -1
Total del pedido $ 6500
Ingrese coordenada x cliente: 6
Ingrese coordenada y cliente: -6
Su pedido sera entregado por Vitacumbia
¿Desea registrar otro pedido?: no

#####  Estadísticas Finales #####
Monto total recaudado $ 6500
Vitacumbia entregó  1 pedidos
San Joaco entregó  0 pedidos
Dignidad entrego 0 Pedidos

# -- Caso 2 -- #
Ingrese numero del plato: 1
Ingrese numero del plato: 1
Ingrese numero del plato: 1
Ingrese numero del plato: 2
Ingrese numero del plato: 2
Ingrese numero del plato: 2
Ingrese numero del plato: 3
Ingrese numero del plato: 3
Ingrese numero del plato: 3
Ingrese numero del plato: -1
Total del pedido $ 31500
Ingrese coordenada x cliente: 4
Ingrese coordenada y cliente: -3
Su pedido sera entregado por Vitacumbia
¿Desea registrar otro pedido?: si

Ingrese numero del plato: 1
Ingrese numero del plato: -1
Total del pedido $ 4000
Ingrese coordenada x cliente: 2
Ingrese coordenada y cliente: -2
Su pedido sera entregado por Dignidad
¿Desea registrar otro pedido?: si

Ingrese numero del plato: 3
Ingrese numero del plato: -1
Total del pedido $ 3500
Ingrese coordenada x cliente: 4
Ingrese coordenada y cliente: -6
Su pedido sera entregado por Vitacumbia
¿Desea registrar otro pedido?: no

#####  Estadísticas Finales #####
Monto total recaudado $ 39000
Vitacumbia entregó  2 pedidos
San Joaco entregó  0 pedidos
Dignidad entrego 1 Pedidos
"""