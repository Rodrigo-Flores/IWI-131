def búsqueda_binaria(lista, elemento):
    while True:
        lista.sort()

        median_index = len(lista)//2 # Indice de la mediana para cada trazo

        # Evaluando
        if len(lista) == 1 and lista[0] != elemento: # No esta en la lista
            return False

        if elemento == lista[median_index]: # Lo encontramos
            return True
        
        # Cortando lista
        if elemento > lista[median_index]: # Se elimina el lado izquierdo
            lista = lista[median_index:]

        elif elemento < lista[median_index]: # Se elimina el lado derecho
            lista = lista[:median_index]