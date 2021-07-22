"""

Autor: Rodrigo Flores
Carrera: Ingenieria Civil Informatica
Curso: IWI131

Observacion (1):
    En mis códigos intento no escribir caracteres especiales, es decir, los del alfabeto hispano, pues suelen haber confunciones y/o 
    errores asociados a esto. En este caso tanto el códido como en los arhcivos anexos a este poseen varios de estos carácteres. Solo
    espero que no explote.

Recomendacion (1):
    Ejecutar desde una terminal.

"""

def avistamientos_por_región(nombre_archivo):
    recuento_regiones_porcentaje = {}
    i = 0 # Este contado nos permite ignorar la primera linea del texto, pues según el formato del enunciado ésta es solo el encabezado
    cantidad_archivos = []
    archivo_principal = open(nombre_archivo, 'r') # Se abre la base de datos

    for linea in archivo_principal: # Se recorre linea a linea
        if i != 0: # Se comienza desde la segunda linea del la base de datos
            datos = linea.strip().split(';') # Se toma la linea actual y la separamos en una lista
            fecha = datos[0].split('-') # Se extrae la fecha de la primera posición de la lista

            nombre_de_region = datos[1] # Nombre de la region en la segunda posición
            cantidad_archivos.append(datos[1])
            mes = fecha[1] # Mes en la segunda posición de la sublista <fecha>
            año = fecha[0] # Año en la primera posición de la sublista <fecha>
            porcentaje = round((int(datos[3]) / int(datos[2])) * 100, 2) # Con un regla de tres, se obtiene el porcentaje
            total_avistamientos = datos[2] # Se obtiene el total de avistamientos

            if nombre_de_region not in recuento_regiones_porcentaje:
                recuento_regiones_porcentaje[nombre_de_region] = []
                recuento_regiones_porcentaje[nombre_de_region].append((porcentaje, mes, año, total_avistamientos))

            else:
                recuento_regiones_porcentaje[nombre_de_region].append((porcentaje, mes, año, total_avistamientos))

        else:
            i+=1  # Se suma uno para luego comenzar desde la segunda linea

    for region in recuento_regiones_porcentaje:
        recuento_regiones_porcentaje[region].sort()
        recuento_regiones_porcentaje[region].reverse()
        nombre_archivo_texto = region + '.txt'

        if len(recuento_regiones_porcentaje[region]) <= 1:
            archivo_de_texto = open(nombre_archivo_texto, "a") # Se abre el reporte de región
            texto_informativo = '''En el mes {mes} de {año} hubo {porcentaje}% de avistamientos confirmados de un total de {total_avistamientos}'''.format(mes=recuento_regiones_porcentaje[region][0][1], año=recuento_regiones_porcentaje[region][0][2], porcentaje=recuento_regiones_porcentaje[region][0][0], total_avistamientos=recuento_regiones_porcentaje[region][0][3])
            archivo_de_texto.write(''.join(texto_informativo)+'\n') # Se escribe una nueva linea
            
            archivo_de_texto.close() # Se cierra el archivo de región

        elif len(recuento_regiones_porcentaje[region]) <= 2:
            archivo_de_texto = open(nombre_archivo_texto, "a") # Se abre el reporte de región
            texto_informativo = '''En el mes {mes} de {año} hubo {porcentaje}% de avistamientos confirmados de un total de {total_avistamientos}'''.format(mes=recuento_regiones_porcentaje[region][0][1], año=recuento_regiones_porcentaje[region][0][2], porcentaje=recuento_regiones_porcentaje[region][0][0], total_avistamientos=recuento_regiones_porcentaje[region][0][3])
            archivo_de_texto.write(''.join(texto_informativo)+'\n') # Se escribe una nueva linea
            texto_informativo = '''En el mes {mes} de {año} hubo {porcentaje}% de avistamientos confirmados de un total de {total_avistamientos}'''.format(mes=recuento_regiones_porcentaje[region][1][1], año=recuento_regiones_porcentaje[region][1][2], porcentaje=recuento_regiones_porcentaje[region][1][0], total_avistamientos=recuento_regiones_porcentaje[region][1][3])
            archivo_de_texto.write(''.join(texto_informativo)+'\n') # Se escribe una nueva linea
            
            archivo_de_texto.close() # Se cierra el archivo de región

        elif len(recuento_regiones_porcentaje[region]) > 2:
            archivo_de_texto = open(nombre_archivo_texto, "a") # Se abre el reporte de región
            texto_informativo = '''En el mes {mes} de {año} hubo {porcentaje}% de avistamientos confirmados de un total de {total_avistamientos}'''.format(mes=recuento_regiones_porcentaje[region][0][1], año=recuento_regiones_porcentaje[region][0][2], porcentaje=recuento_regiones_porcentaje[region][0][0], total_avistamientos=recuento_regiones_porcentaje[region][0][3])
            archivo_de_texto.write(''.join(texto_informativo)+'\n') # Se escribe una nueva linea
            texto_informativo = '''En el mes {mes} de {año} hubo {porcentaje}% de avistamientos confirmados de un total de {total_avistamientos}'''.format(mes=recuento_regiones_porcentaje[region][1][1], año=recuento_regiones_porcentaje[region][1][2], porcentaje=recuento_regiones_porcentaje[region][1][0], total_avistamientos=recuento_regiones_porcentaje[region][1][3])
            archivo_de_texto.write(''.join(texto_informativo)+'\n') # Se escribe una nueva linea
            texto_informativo = '''En el mes {mes} de {año} hubo {porcentaje}% de avistamientos confirmados de un total de {total_avistamientos}'''.format(mes=recuento_regiones_porcentaje[region][2][1], año=recuento_regiones_porcentaje[region][2][2], porcentaje=recuento_regiones_porcentaje[region][2][0], total_avistamientos=recuento_regiones_porcentaje[region][2][3])
            archivo_de_texto.write(''.join(texto_informativo)+'\n') # Se escribe una nueva linea

            archivo_de_texto.close() # Se cierra el archivo de región

    archivo_principal.close() # Se cierra la base de datos

    cantidad_archivos = len(list(set(cantidad_archivos)))

    return cantidad_archivos

try:
    file_name = input('Introduzca el nombre o ruta del archivo (incluyendo la extensión): ')
    print(avistamientos_por_región(file_name)) # Se ejecuta la función

except FileNotFoundError:
    print("El nombre introducida o ruta no existe. Intente nuevamente\n")
    file_name = input('Introduzca el nombre o ruta del archivo (incluyendo la extensión): ')
    print(avistamientos_por_región(file_name)) # Se ejecuta la función

except KeyboardInterrupt:
    print("[ ok ]")