nombre = input()
fecha = int(input())
masa_gramos = round(float(input()),0)

edad = 2021 - fecha
masa_redondeada = int(round(masa_gramos/1000,0))
masa_truncada = int(masa_gramos//1000)

print(f'El candidato {nombre} tiene {edad} años y pesa {masa_redondeada} kilogramos.')
print(f'El candidato {nombre} tiene {edad} años y pesa {masa_truncada} kilogramos.')
