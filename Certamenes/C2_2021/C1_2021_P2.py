def categorizar_sismos(archivo_sismos):
    archivo_sismos = open(archivo_sismos, "r")

    registros_de_magnitud = {}

    for registro in archivo_sismos:
        registro_separado = registro.strip().split(";")

        if float(registro_separado[-2]) >= 2:
            # Datos principales
            fecha_general = registro_separado[0].split("T")
            fecha = fecha_general[0]

            hora_general = fecha_general[1].split(":")
            hora = str(hora_general[0]) + ":" + str(hora_general[1])

            lugar = registro_separado[-1]

            magnitud = registro_separado[-2]

            if registro_separado[-1] not in registros_de_magnitud:
                registros_de_magnitud[registro_separado[-1]] = []
                registros_de_magnitud[registro_separado[-1]].append((magnitud, hora, fecha, lugar))

            else:
                registros_de_magnitud[registro_separado[-1]].append((magnitud, hora, fecha, lugar))

    for i in registros_de_magnitud:
        registros_de_magnitud[i].sort()
        registros_de_magnitud[i].reverse()

    coleccion_magnitudes = {}
    for lugar in registros_de_magnitud:
        for registro in registros_de_magnitud[lugar]:
            if int(float(registro[0])) not in coleccion_magnitudes:
                coleccion_magnitudes[int(float(registro[0]))] = []
                coleccion_magnitudes[int(float(registro[0]))].append(registro)

            else:
                coleccion_magnitudes[int(float(registro[0]))].append(registro)

    for i in coleccion_magnitudes:
        coleccion_magnitudes[i].sort()
        coleccion_magnitudes[i].reverse()

    for magnitud in coleccion_magnitudes:
        file = open("mag"+str(magnitud), "w")

        file.write(''.join(f"Fecha: {coleccion_magnitudes[magnitud][0][2]}; Hora: {coleccion_magnitudes[magnitud][0][1]}; Lugar: {coleccion_magnitudes[magnitud][0][3]}; Magnitud: {coleccion_magnitudes[magnitud][0][0]}") + '\n')
        file.write(''.join(f"Fecha: {coleccion_magnitudes[magnitud][1][2]}; Hora: {coleccion_magnitudes[magnitud][1][1]}; Lugar: {coleccion_magnitudes[magnitud][1][3]}; Magnitud: {coleccion_magnitudes[magnitud][1][0]}") + '\n')
        file.write(''.join(f"Fecha: {coleccion_magnitudes[magnitud][2][2]}; Hora: {coleccion_magnitudes[magnitud][2][1]}; Lugar: {coleccion_magnitudes[magnitud][2][3]}; Magnitud: {coleccion_magnitudes[magnitud][2][0]}") + '\n')

        file.close()

    return len(coleccion_magnitudes)

print(categorizar_sismos("sismos.txt"))