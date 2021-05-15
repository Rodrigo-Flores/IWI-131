def tarifa(tipo_usuario,tipo_ruta):
    if (tipo_ruta == 'Oasis/Tupahue') or (tipo_ruta == 'Tupahue/Oasis'):
        if tipo_usuario.upper() == 'NIÑO':
            return 910

        elif tipo_usuario.upper() == 'ADULTO':
            return 1400

        elif tipo_usuario.upper() == 'TERCERA EDAD':
            return 910
    
    elif (tipo_ruta == 'Oasis/Cumbre') or (tipo_ruta == 'Cumbre/Oasis'):
        if tipo_usuario.upper() == 'NIÑO':
            return 1340

        elif tipo_usuario.upper() == 'ADULTO':
            return 2050

        elif tipo_usuario.upper() == 'TERCERA EDAD':
            return 1340

    elif (tipo_ruta == 'Oasis/Cumbre/Oasis') or (tipo_ruta == 'Cumbre/Oasis/Cumbre'):
        if tipo_usuario.upper() == 'NIÑO':
            return 1760

        elif tipo_usuario.upper() == 'ADULTO':
            return 2700

        elif tipo_usuario.upper() == 'TERCERA EDAD':
            return 1760

    elif tipo_ruta == 'Diario Ilimitado':
        if tipo_usuario.upper() == 'NIÑO':
            return 3430

        elif tipo_usuario.upper() == 'ADULTO':
            return 5250

        elif tipo_usuario.upper() == 'TERCERA EDAD':
            return 3430

    else: 
        print('NO EXISTE ESTE TIPO DE USUARIO O RUTA')
        return 0

total_dinero = int(input('Ingrese su dinero total:'))
while True:
    tipo_usuario = input('Tipo de Usuario:')
    tipo_ruta = input('Tipo de Ruta:')

    precio = int(tarifa(tipo_usuario, tipo_ruta))

    if total_dinero >= precio:
        total_dinero -= precio
        if total_dinero > 1400:
            print('Le quedan $' + str(total_dinero))
        
        else:
            print('Ya no puede comprar más tickets. Le sobraron', total_dinero)
            break

    elif (total_dinero < precio) and (total_dinero > 0):
        print('NO TIENE DINERO SUFICIENTE')

    elif total_dinero < 910:
        print('Ya no puede comprar más tickets. Le sobraron', total_dinero)
        break
        
