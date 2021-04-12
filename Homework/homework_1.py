# Solicitando los datos de "alimento", para almacenarlos en variables.
nevarro_nummies = float(input("Nevarro Nummies consumidad (en unidades): "))
space_soup = float(input("Space Soup consumida (en [ml]): "))
carne_de_rana = float(input("Carne de rana consumida (en [g]): "))

# Nevarro Nummies, por unidad de 11 [g]
nevarro_nummies_grasa = 1.90 # [g]
nevarro_nummies_carbohidratos = 6.00 # [g]
nevarro_nummies_proteinas = 0.80 # [g]

# Space Soup, por porcion de 256 [ml]
space_soup_grasas = 10.0 # [g]
space_soup_carbohidratos = 12.0 # [g]
space_soup_proteinas = 11.0 # [g]

# Carne de rana, por cada 100[g]
carne_de_rana_grasas = 0.30 # [g]
carne_de_rana_carbohidratos = 0.00 # [g]
carne_de_ranaproteinas = 16.0 # [g]

"""
Gramos a Calorias
1[g] Grasas = 9[calorias]
1[g] Carbohidratos = 4[calorias]
1[g] Proteínas = 4[calorias]
"""

def N_N(nevarro_nummies):
    grasa_total_n = nevarro_nummies * nevarro_nummies_grasa
    carbohidratos_total_n = nevarro_nummies * nevarro_nummies_carbohidratos
    proteinas_total_n = nevarro_nummies * nevarro_nummies_proteinas

    return grasa_total_n, carbohidratos_total_n, proteinas_total_n

def S_S():
    grasa_total_s = nevarro_nummies * nevarro_nummies_grasa
    carbohidratos_total_s = nevarro_nummies * nevarro_nummies_carbohidratos
    proteinas_total_s = nevarro_nummies * nevarro_nummies_proteinas

    return grasa_total_s, carbohidratos_total_s, proteinas_total_s

def C_R():
    grasa_total_c = nevarro_nummies * nevarro_nummies_grasa
    carbohidratos_total_c = nevarro_nummies * nevarro_nummies_carbohidratos
    proteinas_total_c = nevarro_nummies * nevarro_nummies_proteinas

    return grasa_total_c, carbohidratos_total_c, proteinas_total_c
