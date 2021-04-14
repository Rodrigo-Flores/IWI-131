nombre = input()
fecha = int(input())
masa_gramos = round(float(input()),1)

edad = 2021 - fecha
masa_final = round(masa_gramos/1000,2)

print(f'El candidato {nombre} tiene {edad} años y pesa {masa_final} kilogramos.')
