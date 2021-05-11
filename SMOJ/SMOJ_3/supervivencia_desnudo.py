def calorias(dificultad, dias):
    if dificultad == "F":
        calo = dias * 1000

    if dificultad == "M":
        calo = dias * 2500

    elif dificultad == "D":
        calo = dias * 500

    return calo