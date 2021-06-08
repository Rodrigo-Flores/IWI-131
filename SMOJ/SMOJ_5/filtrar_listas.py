def filtrar(original, eliminar):
    lista = []
    
    for i in original:
        if i not in eliminar and i not in lista:
            lista.append(i)
            
    return lista