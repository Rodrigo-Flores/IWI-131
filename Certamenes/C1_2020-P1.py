def dia_de_la_semana(dd, mm, aaaa):
    a = (14-mm)//12
    y = aaaa - a
    m = mm + (12*a) - 2 
    d = int((dd + y + (y//4) - (y//100) + (y//400) + ((31*m)//12))%7)

    if d == 0:
        return 'Domingo'

    elif d == 1:
        return 'Lunes'

    elif d == 2:
        return 'Martes'

    elif d == 3:
        return 'Miércoles'

    elif d == 4:
        return 'Jueves'

    elif d == 5:
        return 'Viernes'

    elif d == 6:
        return 'Sábado'

people = '16052000,Sofia;29022000,Silvia;01082000,Andrea;28042000,Paula;04102000,Eduardo;26062001,Pedro;11072001,Federico;03112001,Claudia;20052001,Lucas;24061999,Gabriel;04101999,Camila'
people += ';'

print('Fecha de nacimiento')
dd = int(input('Día: '))
mm = int(input('Mes: '))
aaaa = int(input('Año: '))

fecha_personal = dia_de_la_semana(dd,mm,aaaa)

print('Naciste un', fecha_personal)
print('Amigos a invitar: ')

flag_out = True
i=0
prev = 0
while i < len(people):
    j = i
    individual = ''
    while people[j] != ';':
        individual += people[j]
        j+=1

    dd2 = int(individual[0:2])

    mm2 = int(individual[2:4])

    aaaa2 = int(individual[4:7])

    nombre = individual[9:]

    fecha_final = dia_de_la_semana(dd2,mm2,aaaa2)

    if fecha_final == fecha_personal:
        amigo = nombre
        print(nombre)

    i = j + 1

        
