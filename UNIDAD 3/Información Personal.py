# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Valentina Villalva",
    "edad": 38,
    "ciudad": "Cuenca",
    "profesion": "Medico Pediatra"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor al diccionario para "profesion"
informacion_personal["profesion"] = "Medico Pediatra"

# Verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0971234667"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
