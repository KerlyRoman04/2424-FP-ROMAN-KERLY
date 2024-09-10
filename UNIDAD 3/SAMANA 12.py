# Crear una matriz 3D para almacenar datos de humedad
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
humedades = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "humidity": 65},
            {"day": "Martes", "humidity": 68},
            {"day": "Miércoles", "humidity": 70},
            {"day": "Jueves", "humidity": 72},
            {"day": "Viernes", "humidity": 75},
            {"day": "Sábado", "humidity": 78},
            {"day": "Domingo", "humidity": 80}
        ],
        [   # Semana 2
            {"day": "Lunes", "humidity": 67},
            {"day": "Martes", "humidity": 70},
            {"day": "Miércoles", "humidity": 73},
            {"day": "Jueves", "humidity": 74},
            {"day": "Viernes", "humidity": 76},
            {"day": "Sábado", "humidity": 79},
            {"day": "Domingo", "humidity": 82}
        ],
        [   # Semana 3
            {"day": "Lunes", "humidity": 66},
            {"day": "Martes", "humidity": 69},
            {"day": "Miércoles", "humidity": 71},
            {"day": "Jueves", "humidity": 73},
            {"day": "Viernes", "humidity": 77},
            {"day": "Sábado", "humidity": 80},
            {"day": "Domingo", "humidity": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "humidity": 68},
            {"day": "Martes", "humidity": 71},
            {"day": "Miércoles", "humidity": 74},
            {"day": "Jueves", "humidity": 75},
            {"day": "Viernes", "humidity": 78},
            {"day": "Sábado", "humidity": 80},
            {"day": "Domingo", "humidity": 83}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "humidity": 55},
            {"day": "Martes", "humidity": 58},
            {"day": "Miércoles", "humidity": 60},
            {"day": "Jueves", "humidity": 62},
            {"day": "Viernes", "humidity": 65},
            {"day": "Sábado", "humidity": 68},
            {"day": "Domingo", "humidity": 70}
        ],
        [   # Semana 2
            {"day": "Lunes", "humidity": 57},
            {"day": "Martes", "humidity": 60},
            {"day": "Miércoles", "humidity": 63},
            {"day": "Jueves", "humidity": 65},
            {"day": "Viernes", "humidity": 67},
            {"day": "Sábado", "humidity": 70},
            {"day": "Domingo", "humidity": 72}
        ],
        [   # Semana 3
            {"day": "Lunes", "humidity": 56},
            {"day": "Martes", "humidity": 59},
            {"day": "Miércoles", "humidity": 62},
            {"day": "Jueves", "humidity": 64},
            {"day": "Viernes", "humidity": 66},
            {"day": "Sábado", "humidity": 69},
            {"day": "Domingo", "humidity": 71}
        ],
        [   # Semana 4
            {"day": "Lunes", "humidity": 58},
            {"day": "Martes", "humidity": 61},
            {"day": "Miércoles", "humidity": 64},
            {"day": "Jueves", "humidity": 66},
            {"day": "Viernes", "humidity": 68},
            {"day": "Sábado", "humidity": 70},
            {"day": "Domingo", "humidity": 73}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "humidity": 80},
            {"day": "Martes", "humidity": 83},
            {"day": "Miércoles", "humidity": 85},
            {"day": "Jueves", "humidity": 87},
            {"day": "Viernes", "humidity": 89},
            {"day": "Sábado", "humidity": 91},
            {"day": "Domingo", "humidity": 93}
        ],
        [   # Semana 2
            {"day": "Lunes", "humidity": 81},
            {"day": "Martes", "humidity": 84},
            {"day": "Miércoles", "humidity": 86},
            {"day": "Jueves", "humidity": 88},
            {"day": "Viernes", "humidity": 90},
            {"day": "Sábado", "humidity": 92},
            {"day": "Domingo", "humidity": 94}
        ],
        [   # Semana 3
            {"day": "Lunes", "humidity": 79},
            {"day": "Martes", "humidity": 82},
            {"day": "Miércoles", "humidity": 84},
            {"day": "Jueves", "humidity": 86},
            {"day": "Viernes", "humidity": 88},
            {"day": "Sábado", "humidity": 90},
            {"day": "Domingo", "humidity": 92}
        ],
        [   # Semana 4
            {"day": "Lunes", "humidity": 82},
            {"day": "Martes", "humidity": 85},
            {"day": "Miércoles", "humidity": 87},
            {"day": "Jueves", "humidity": 89},
            {"day": "Viernes", "humidity": 91},
            {"day": "Sábado", "humidity": 93},
            {"day": "Domingo", "humidity": 95}
        ]
    ]
]

# Calcular el promedio de humedad para cada ciudad y semana
for ciudad in humedades:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['humidity']
        print(suma / 7)  # Imprimir el promedio de la semana
