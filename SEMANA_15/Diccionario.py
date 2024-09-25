# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor al diccionario que represente la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)


