def calcular_temperatura_promedio(datos_temperatura):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Parámetros:
    datos_temperatura (dict): Diccionario donde las claves son los nombres de las ciudades
                              y los valores son listas de listas con las temperaturas
                              de cada semana.

    Retorna:
    dict: Diccionario donde las claves son los nombres de las ciudades y los valores
          son las temperaturas promedio calculadas.
    """
    temperaturas_promedio = {}

    for ciudad, semanas in datos_temperatura.items():
        suma_total = 0
        conteo_total = 0

        for semana in semanas:
            suma_total += sum(semana)
            conteo_total += len(semana)

        promedio = suma_total / conteo_total if conteo_total != 0 else 0
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Ejemplo de uso
datos = {
    'Ciudad1': [
        [20, 22, 24],  # Semana 1
        [21, 23, 25],  # Semana 2
        [22, 24, 26]  # Semana 3
    ],
    'Ciudad2': [
        [30, 32, 34],  # Semana 1
        [31, 33, 35],  # Semana 2
        [32, 34, 36]  # Semana 3
    ],
    'Ciudad3': [
        [10, 12, 14],  # Semana 1
        [11, 13, 15],  # Semana 2
        [12, 14, 16]  # Semana 3
    ]
}

resultados = calcular_temperatura_promedio(datos)
print(resultados)

