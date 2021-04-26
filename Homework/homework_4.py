nombre_sucursal = input()
coordenadas = input()

# Sucursales y acumulacciones
san_joaco = 0
vitacumbia = 0
dignidad = 0

# Platos y total
carnivoro = 4000 # Plato 1
vegetariano = 3000 # Plato 2
vegano = 3500 # Plato 3
total_pedido = 0

pedido = 0

flag_in = True
flag_out = True

while flag_out:
    while flag_in:
        pedido = input()

        if pedido == "1":
            total_pedido += carnivoro

        elif pedido == "2":
            total_pedido += vegetariano

        elif pedido == "3":
            total_pedido += vegano

        elif pedido == "-1":
            flag_in = False

            print("Total del pedido $", total_pedido)

        coordenada_x = input("Ingrese coordenada x cliente: ")
        coordenada_y = input("Ingrese coordenada y cliente: ")

        if coordenada_x == 6 and coordenada_y == -3: # Vitacumbia
            vitacumbia += 1

        elif coordenada_x == -1 and coordenada_y == 5: # San Joaco
            vitacumbia += 1

        elif coordenada_x == 0 and coordenada_y == 0: # Dignidad
            vitacumbia += 1
        
    continuar = input("¿Desea registrar otro pedido?: ")

    if continuar == "si":
        pass

    else:
        flag_out = False

print("#####  Estadísticas Finales #####")
print("Monto total recaudado $", total_pedido)
print("Vitacumbia entregó ", vitacumbia,"pedidos")
print("San Joaco entregó ", san_joaco, "pedidos")
print("Dignidad entrego", dignidad, "Pedidos")

"""
Nombre sucursal 1:  Vitacumbia
Coordenada x:   6
Coordenada y:   -3

Nombre sucursal 2:  San Joaco
Coordenada x:   -1
Coordenada y:   5

Nombre sucursal 3:  Dignidad
Coordenada x:   0
Coordenada y:   0

"""
    
        

