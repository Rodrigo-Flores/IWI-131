"""

Autor: Rodrigo Flores
Carrera: Ingenieria Civil Informatica
Curso: IWI131

Observacion (1):
    Este codigo no posee, en lo posible, ninguna tilde ni caracter fuera del alfabeto anglosajon.
    Asi se evitan errores innecesarios.

Recomendacion (1):
    Ejecutar desde una terminal.
    
"""

# -------------------------------------------------------------------- o --------------------------------------------------------------------------#

def disparo(tablero, barcos, fila, columna):
    fire = 0
    for barco in barcos: # Seleccionamos un barco
        for n in range(barco[0]): # Vamos a recorrer el largo del barco
            if barco[1] == 2: # Caso horizontal
                if fila == barco[2] and columna == (barco[3]+n):
                    tablero[fila][columna] = 'O'
                    fire+=1

            elif barco[1] == 1: # Caso vertical
                if fila == (barco[2]+n) and columna == barco[3]:
                    tablero[fila][columna] = 'O'
                    fire+=1

    if fire == 0:
        tablero[fila][columna] = ' '

def score(tablero, barcos):
    final = 0
    for barco in barcos: # Seleccionamos un barco
        c = 0
        for n in range(barco[0]):
            if barco[1] == 2: # Caso horizontal
                if tablero[barco[2]][barco[3]+n] == 'X':
                    c+=1

            elif barco[1] == 1: # Caso vertical
                if tablero[barco[2]+n][barco[3]] == 'X':
                    c+=1

        if c == barco[0]:
            final+=1

    return final
                    

def destruidos(tablero, barcos):
    destruido = 0
    for barco in barcos: # Seleccionamos un barco
        count = 0
        for n in range(barco[0]): # Vamos a recorrer el largo del barco
            if barco[1] == 2: # Caso horizontal
                if tablero[barco[2]][barco[3]+n] == 'O':
                    count+=1

            if barco[1] == 1: # Caso vertical
                if tablero[barco[2]+n][barco[3]] == 'O':
                    count+=1

        if count == barco[0]: # Si y solo si los disparos acertados corresponden al largo del barco se destruye
            destruido+=1
            for destroy in range(barco[0]):
                if barco[1] == 2: # Caso horizontal
                    tablero[barco[2]][barco[3]+destroy] = 'X'

                if barco[1] == 1: # Caso vertical
                    tablero[barco[2]+destroy][barco[3]] = 'X'

                
    return score(tablero, barcos)

mostrar_solucion = 1 # Para mostrar barcos en el tablero

# -------------------------------------------------------------------- o --------------------------------------------------------------------------#

##################################################
#                                                #
#  NO MODIFIQUE EL CÓDIGO A PARTIR DE ESTE PUNTO #
#                                                #
##################################################

import random as rd

# Función que muestra el tablero con el formato deseado para la pantalla
def show(tablero):
    print("\n  123456789")
    for i in range(9):
        fila_texto = " "
        for j in tablero[i]:
            fila_texto += str(j)
        print(chr(65+i)+fila_texto)

# Creación del tablero (inicialmente únicamente con "-" en todas las posiciones)
tablero = []
board = []
for i in range(9):
    fila = []
    for j in range(9):
        fila.append("-")
    tablero.append(fila)
    board.append(list(fila))

# Creación de los barcos con orientación y posición aleatorias
barcos = []
length = [2,3,3,4,5]
for i in range(5):
    l = length[i]
    orientation = rd.randint(1,2)
    if orientation == 1:
        flag = True
        while flag:
            row = rd.randint(0,9-l)
            column = rd.randint(0,8)
            empty = True
            for j in range(l):
                empty = empty and board[row+j][column] != "X"
            if empty:
                flag = False
        for j in range(l): board[row+j][column] = "X"
    else:
        flag = True
        while flag:
            row = rd.randint(0,8)
            column = rd.randint(0,9-l)
            if "X" not in board[row][column:column+l]:
                flag = False
        for j in range(l): board[row][column+j] = "X"
    barcos.append([l,orientation,row,column])
print(barcos)
# Se muestra la solución al inicio en caso de que se haya seleccionado esta opción
if mostrar_solucion == 1:
    print("Solución:")
    show(board)
    print("\n\n")

# Ciclo principal del programa donde se reciben los disparos, se validan y se llama a la función disparo()
print("¡Bienvenido a Solitary Battleship!")
destroyed = 0
while destroyed < 5:
    not_valid = True
    while not_valid:
        turn = input("\n¿Que casilla desea disparar? (Ejemplo: A1): ")
        not_valid = False
        if len(turn) != 2:
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("A" <= turn[0] and turn[0] <= "I"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        elif not("1" <= turn[1] and turn[1] <= "9"):
            not_valid = True
            print("Ingrese una casilla válida por favor.")
        else:
            fila = "ABCDEFGHI".index(turn[0])
            columna = int(turn[1])-1
            if tablero[fila][columna] != "-":
                not_valid = True
                print("Ya ha disparado a esta casilla.")
    disparo(tablero, barcos, fila, columna)
    destroyed = destruidos(tablero, barcos)
    show(tablero)
    print("\n"+str(destroyed)+" barcos destruidos.")
    # Fin del juego
    if destroyed == 5:
        print("Felicidades, juego terminado.")
