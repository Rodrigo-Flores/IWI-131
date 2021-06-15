# Lista de amigos
amigos = [('Mojojojo',('mechero','kawaii','furro','lolero')),
('Otaku-taku',('otaku','avaro','lolero','leal')),
('Maiga',('paciente','otaku','leal')),
('Seiya',('leal','acusete')),
('Vegeta',('otaku','avaro')),
('Sneki',('leal','kawaii','vtuver')),
('Kalila',('lolero','kawaii')),
('Grogu',('avaro','kawaii','lolero','otaku')),
('Freezer',('acusete','furro','otaku','lolero'))]

# Listas de caracteristicas
características = [('kawaii',10),('leal',20),('acusete',-10),
                   ('avaro',-15),('respetuoso',20),('otaku',25),
                   ('lolero',25),('furro',-50),('vtuver',25),
                   ('mechero',-30)]


def obtener_valor_característica(características, buscada):
   for object in características:
      if object[0] == buscada: # Encontramos la caracteristica buscada
         return object[1] # Retornamos el valor de dicha caracteristica

   return 0 # Si no la encontramos retornamos 0

# print(obtener_valor_característica(características, "vtuver"))
# print(obtener_valor_característica(características, "puntual"))

def puntaje_amigo(amigo, características):
   points = 0 # Acumulador de puntos
   for feature in amigo[1]: 
      points+=obtener_valor_característica(características, feature) # Se le suma el valor de cada caracteristica

   return points # Retornamos los puntos totales

# print(puntaje_amigo(('Vegeta',('otaku','avaro')),características))

def lolero(amigo): # Funcion para verificar que el amigo es lolero
   if 'lolero' in amigo[1]: # Si lolero es una de sus caracteristicas
      return True # Retornamos True

   return False # Si no, se retorna False

scores = []
for friend in amigos:
   if lolero(friend): # Si es lolero
      temp_score = puntaje_amigo(friend, características) # Se obtiene el puntaje del amigo
      scores.append([temp_score, friend[0]]) # Se añade el puntaje y el nombre del amigo

scores.sort() # Ordenamos la lista de manor a mayor
scores.reverse() # revertimos el orden, para que los dos mayores queden al principio. Posiciones 0 y 1 en la lista

print(
   'Equipo seleccionado:',
   '\n' +
   str(scores[0][1]), str(scores[0][0]), # Primer puntjae mas alto
   '\n' +
   str(scores[1][1]), str(scores[1][0]) # Segundo puntaje mas alto
)
