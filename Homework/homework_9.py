"""

Autor: Rodrigo Flores
Carrera: Ingenieria Civil Informatica
Curso: IWI131

Observacion (1):
    Este codigo no posee, en lo posible, ninguna tilde ni caracter fuera del alfabeto anglosajon.
    Asi se evitan errores innecesarios.

Observación (2):
    El código no está preparado para casos de pruebas fuera de los permitidos por el enunciado de la tarea, pues dentro de los parámetros
    de esta, se dice claramente que hya ciertas cosas a considerar como:
    
    "En todo momento puede suponer que los datos ingresados serán correctos y con el formato adecuado, 
    y que nunca se intentará vacunar a una persona más de 2 veces."

Recomendacion (1):
    Ejecutar desde una terminal.
    
"""

day = int(input('Día: '))
month = int(input('Mes: '))
year = int(input('Año: '))

date = (year,month,day) 

dosis = {}
vacunas = {}
personal = {}
repeat = True
while repeat:
    rut = input('RUT: ')

    # Informacion personal
    if rut not in dosis:
        age = int(input('Edad: '))
        vaccine_type = input('Tipo vacuna: ')

        dosis[rut] = [age,date] # Se registra la edad y la primera dosis del paciente

    elif (rut in dosis) and (len(dosis[rut]) == 2):
        print('Segunda dosis. Paciente debe ser inoculado con:', personal[rut])
        dosis[rut].append(date) # Se añade la segunda dosis del paciente

    # Aqui se guarda el tipo de vacuna ocupada por persona.
    if rut not in personal:
            personal[rut] = vaccine_type

    # Si y solo si la dosis se completa (2 vacunas) se añade al diccionario
    if len(dosis[rut]) == 3:
        if personal[rut] not in vacunas:
            vacunas[personal[rut]] = [rut]

        elif personal[rut] in vacunas:
            vacunas[personal[rut]].append(rut)

    # Para repetir el registro de una inoculación
    repeat = input('¿Desea continuar? (s/n): ').upper()
    if repeat == 'N':
        repeat = False


age_summary = {} # Aqui se guarda el conteo por edades

# Aqui contamos la cantidad de pacientes inoculados completamente y se clasifican por edad
for i in dosis:
    if len(dosis[i]) == 3:
        if dosis[i][0] not in age_summary:
            age_summary[dosis[i][0]] = 1

        elif dosis[i][0] in age_summary:
            age_summary[dosis[i][0]]+=1

print('\n' + 'Edades con más personas con esquema de inoculación completo: ')

top = [] # Aqui se guardan las edades y sus respectivos conteos
for i in age_summary: # 
    top.append([age_summary[i], i])

top.sort() # Se ordena la lista de menor a mayor
top.reverse() # Damos vuelta el orden, entonces queda de mayor a menor

print(
    top[0][1], 'años:', top[0][0], 'personas', # Primero mayor 
    '\n' + str(top[1][1]), 'años:' , top[1][0], 'personas', # Segundo mayor
    '\n' + str(top[2][1]), 'años:' , top[2][0], 'personas' # Tercer mayor
)
