# Vamos a crear un nuevo archivo de texto llamado "my_notes.txt" y agregar las notas personales actualizadas.
# Luego, leeremos y mostraremos cada línea del archivo en la consola.

# Creación y escritura en el archivo
with open("/mnt/data/my_notes.txt", "w") as file:
    # Escribimos las tres notas personales proporcionadas
    file.write("1. Soy una persona que le encanta los animalitos y por eso tengo 3 perros y 3 gatitos.\n")
    file.write("2. Sufro de ansiedad, pero he logrado poco a poco controlarlo.\n")
    file.write("3. Me gusta cocinar y viajar mucho.\n")

# Lectura del archivo línea por línea utilizando readline
with open("/mnt/data/my_notes.txt", "r") as file:
    # Leer y mostrar cada línea del archivo
    line = file.readline()  # Lee la primera línea
    while line:
        print(line.strip())  # Mostramos la línea eliminando saltos de línea extra
        line = file.readline()  # Lee la siguiente línea

# El archivo se cierra automáticamente tras su lectura.


