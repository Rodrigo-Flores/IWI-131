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

    # Do you want to add a new register?
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

print()
for i in age_summary:
    print(i, 'años:', age_summary[i], 'personas')


'''

vacunas = {
"Sinovac":["11.111.111-1", "12.345.678-9"],
"Pfizer": ["8.978.657-3"],
"CanSino": ["13.789.456-k"]
}


dosis = {
"11.111.111-1":[55,(2021,4,11),(2021,5,10)],
"12.345.678-9":[47,(2021,6,3)],
"8.978.657-3":[79,(2021,3,23)],
"13.789.456-k":[40,(2021,5,18),(2021,6,10)]
}

'''
