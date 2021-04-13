# Solicitando los datos de "alimento", para almacenarlos en variables.
nevarro_nummies = float(input("Nevarro Nummies consumidas (en unidades): "))
space_soup = float(input("Space Soup consumida (en [ml]): "))
carne_de_rana = float(input("Carne de rana consumida (en [g]): "))

# Nevarro Nummies, por unidad de 11 [g]
nevarro_nummies_grasas = 1.90 * nevarro_nummies # [g]
nevarro_nummies_carbohidratos = 6.00 * nevarro_nummies # [g]
nevarro_nummies_proteinas = 0.80 * nevarro_nummies # [g]

# Space Soup, por porcion de 256 [ml]
space_soup_grasas = (10.0/285) * space_soup # [g]
space_soup_carbohidratos = (12.0/285) * space_soup # [g]
space_soup_proteinas = (11.0/285) * space_soup # [g]

# Carne de rana, por cada 100[g]
carne_de_rana_grasas = (0.30/100) * carne_de_rana # [g]
carne_de_rana_carbohidratos = (0.00/100) * carne_de_rana # [g]
carne_de_rana_proteinas = (16.0/100) * carne_de_rana # [g]

# Sumando el total de grasa
total_grasa = round(nevarro_nummies_grasas + space_soup_grasas + carne_de_rana_grasas,2)

# Sumando el total de carbohidratos
total_carbohidratos = round(nevarro_nummies_carbohidratos + space_soup_carbohidratos + carne_de_rana_carbohidratos,2)

# Sumando el total de proteinas
total_proteinas = round(nevarro_nummies_proteinas + space_soup_proteinas + carne_de_rana_proteinas,2)

# Calculando las calorias consumidas a partir de los datos entregados
total_calorias = round((9*total_grasa)+(4*total_carbohidratos)+(4*total_proteinas),)

# Imprimiento en pantalla la información solicitada.
print("Goru ha consumido:")
print(total_grasa,"[g] de grasas")
print(total_carbohidratos,"[g] de carbohidratos")
print(total_proteinas,"[g] de proteinas")
print("dando un total de")
print(total_calorias,"[calorias]")
