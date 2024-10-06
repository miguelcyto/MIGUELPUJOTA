#accedemos a nustro archivo creado
#imprimimos su contenido
file=open("my_notes.txt", "r")
print(file)
#usamos with para leer el contenido del archivo en una sola linea
with open('my_notes.txt', 'r') as file:
  linea = file.readlines()
  print(linea)
#usamos for para desplegar el contenido del rachivo en listado
  for l in linea:
      print(l.replace("\n", ""))
