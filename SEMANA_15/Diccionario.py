# Crear un diccionario llamado informacion_personal con las claves nombre, edad, ciudad,profesion
informacion_personal = {"Nombre": "Miguel Pujota","Edad": 33,"Ciudad": "Quito","Profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["Ciudad"] = "Cuenca"

# Agregar una nueva clave-valor al diccionario  que represente la "profesion"
informacion_personal["Profesion"] = "Militar"

# Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
# en este caso vamos a utilizar IF para verificar si existe o no el numero de telefono
# en el caso de no existir agregaremos a nuestro diccionario.
if "telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "0998242901"

# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal["Edad"]

# una vez realizado los cambios vamos a imprimir el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)


