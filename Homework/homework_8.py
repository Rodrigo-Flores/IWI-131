personas = [
   ('Edsger Dijkstra', (1930, 5, 11), 'Holanda'),
   ('Alan Turing', (1912, 6, 23), 'Inglaterra'),
   ('Alonzo Church', (1903, 6, 14), 'Estados Unidos'),
   ('Stephen Cook', (1939, 12, 14), 'Estados Unidos'),
   ('Guido van Rossum', (1956, 1, 31), 'Holanda'),
   ('Tony Hoare', (1934, 1, 11), 'Inglaterra'),
   ('Grace Hopper', (1906, 12, 9), 'Estados Unidos'),
   ('Charles Babbage', (1791, 12, 26), 'Inglaterra'),
   ('Donald Knuth', (1938, 1, 10), 'Estados Unidos')
]

amigos = [('Mojojojo',('mechero','kawaii','furro','lolero')),
('Otaku-taku',('otaku','avaro','lolero','leal')),
('Maiga',('paciente','otaku','leal')),
('Seiya',('leal','acusete')),
('Vegeta',('otaku','avaro')),
('Sneki',('leal','kawaii','vtuver')),
('Kalila',('lolero','kawaii')),
('Grogu',('avaro','kawaii','lolero','otaku')),
('Freezer',('acusete','furro','otaku','lolero'))]

características = [('kawaii',10),('leal',20),('acusete',-10),
                   ('avaro',-15),('respetuoso',20),('otaku',25),
                   ('lolero',25),('furro',-50),('vtuver',25),
                   ('mechero',-30)]

def obtener_valor_característica(características, buscada):
   for object in características:
      if object[0] == buscada:
         return object[1]

   return 0

# print(obtener_valor_característica(características, "vtuver"))
# print(obtener_valor_característica(características, "puntual"))

def puntaje_amigo(amigo, características):
   points = 0
   for feature in amigo[1]:
      points+=obtener_valor_característica(características, feature)

   return points

# print(puntaje_amigo(('Vegeta',('otaku','avaro')),características))

def lolero(amigo):
   if 'lolero' in amigo[1]:
      return True

   return False

scores = []
for friend in amigos:
   if lolero(friend):
      temp_score = puntaje_amigo(friend, características)
      scores.append([temp_score, friend[0]])

scores.sort()
scores.reverse()

print(
   'Equipo seleccionado:',
   '\n' +
   str(scores[0][1]), str(scores[0][0]),
   '\n' +
   str(scores[1][1]), str(scores[1][0])
)
