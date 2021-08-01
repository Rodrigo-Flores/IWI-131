def sismos_por_pais(archivo_sismos):
    archivo_sismos = open(archivo_sismos, "r")
    archivo_eeuu = open("estados_eeuu.txt", "r")

    lista_estados_eeuu= []
    for estado in archivo_eeuu:
        lista_estados_eeuu.append(estado.strip())

    registros_por_pais = {}

    for registro in archivo_sismos:
        registro_separado = registro.strip().split(";")

        if float(registro_separado[-2]) >= 2:
            if registro_separado[-1] in lista_estados_eeuu:
                if "EEUU" in registros_por_pais:
                    registros_por_pais["EEUU"][0] += 1

                elif "EEUU" not in registros_por_pais:
                    registros_por_pais["EEUU"] = [1, "EEUU"]

            else:
                if registro_separado[-1] in registros_por_pais:
                    registros_por_pais[registro_separado[-1]][0] += 1

                elif registro_separado[-1] not in registros_por_pais:
                    registros_por_pais[registro_separado[-1]] = [1, registro_separado[-1]]

    top = []
    for i in registros_por_pais:
        top.append(tuple(registros_por_pais[i]))

    top.sort()
    top.reverse()

    return top

print(sismos_por_pais("sismos.txt"))
