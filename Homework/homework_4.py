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

## Platos y total
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

        if pedido == "1":
            total_pedido += carnivoro

        elif pedido == "2":
            total_pedido += vegetariano

        elif pedido == "3":
            total_pedido += vegano

        elif pedido == "-1":
            flag_in = False

            print("Total del pedido $", total_pedido)

    # Solicitando coordenada al cliente
    coordenada_x = float(input("Ingrese coordenada x cliente: "))
    coordenada_y = float(input("Ingrese coordenada y cliente: "))

    # Calculando distancia entre dos puntos del plano
    distancia_cliente_a_VC = ((x_vitacumbia-coordenada_x)**2 + (y_vitacumbia-coordenada_y)**2)**1/2 # Vitacumbia
    distancia_cliente_a_SJ = ((x_san_joaco-coordenada_x)**2 + (y_san_joaco-coordenada_y)**2)**1/2 # San Joaco
    distancia_cliente_a_DG = ((x_dignidad-coordenada_x)**2 + (y_dignidad-coordenada_y)**2)**1/2 # Dignidad
    
    # Loop para ver la mejor ubucaion para realizar la entrega
    while flag_menor:
        # Vitacumbia es la mejor distancias hasta el cliente
        if distancia_cliente_a_VC < distancia_cliente_a_SJ and distancia_cliente_a_VC < distancia_cliente_a_DG:
            menor_distancia = distancia_cliente_a_VC # Eligiendo nueva menor distancia
            vitacumbia += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por Vitacumbia")
            flag_menor = False

        # San Joaco es la mejor distancias hasta el cliente
        elif distancia_cliente_a_SJ < distancia_cliente_a_VC and distancia_cliente_a_SJ < distancia_cliente_a_DG:
            menor_distancia = distancia_cliente_a_SJ # Eligiendo nueva menor distancia
            san_joaco += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por San Joaco")
            flag_menor = False

        # Dignidad es la mejor distancias hasta el cliente
        elif distancia_cliente_a_DG < distancia_cliente_a_VC and distancia_cliente_a_DG < distancia_cliente_a_SJ:
            menor_distancia = distancia_cliente_a_DG # Eligiendo nueva menor distancia
            dignidad += 1 # Sumando pedidos al contador del local
            print("Su pedido sera entregado por Dignidad")
            flag_menor = False

    total_recaudado += total_pedido

    continuar = input("¿Desea registrar otro pedido?: ")
    print()

    if continuar == "si":
        pass

    else:
        flag_out = False

# Imprimiendo en pantalla los datos solicitados
print("#####  Estadísticas Finales #####")
print("Monto total recaudado $", total_recaudado)
print("Vitacumbia entregó ", vitacumbia,"pedidos")
print("San Joaco entregó ", san_joaco, "pedidos")
print("Dignidad entrego", dignidad, "Pedidos")

# Fin del programa