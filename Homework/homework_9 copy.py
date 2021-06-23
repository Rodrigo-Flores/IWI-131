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

    # Personal User's Info
    if rut not in dosis:
        age = int(input('Edad: '))
        vaccine_type = input('Tipo vacuna: ')

        dosis[rut] = [age,date]

    elif (rut in dosis) and (len(dosis[rut]) == 2):
        print('Segunda dosis. Paciente debe ser inoculado con:', personal[rut])
        dosis[rut].append(date)

    if rut not in personal:
            personal[rut] = vaccine_type

    if len(dosis[rut]) == 3:
        if personal[rut] not in vacunas:
            vacunas[personal[rut]] = [rut]

        elif personal[rut] in vacunas:
            vacunas[personal[rut]].append(rut)

    # Para repetir el registro de una inoculación
    repeat = input('¿Desea continuar? (s/n): ').upper()
    if repeat == 'N':
        repeat = False


age_summary = {}
for i in dosis:
    if len(dosis[i]) == 3:
        if dosis[i][0] not in age_summary:
            age_summary[dosis[i][0]] = 1

        elif dosis[i][0] in age_summary:
            age_summary[dosis[i][0]]+=1

print('\n' + 'Edades con más personas con esquema de inoculación completo: ')
top = []
for i in age_summary:
    top.append([age_summary[i], i])

    # print(i, 'años:', age_summary[i], 'personas')
top.sort()
top.reverse()

print(
    top[0][1], 'años:', top[0][0], 'personas',
    '\n' + str(top[1][1]), 'años' , top[1][0], 'personas',
    '\n' + str(top[2][1]), 'años' , top[2][0], 'personas'
)
