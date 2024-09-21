def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
monto1 = 100.00  # Monto total de la primera compra
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

print(f"Monto total: ${monto1:.2f}")
print(f"Descuento: ${descuento1:.2f} (10%)")
print(f"Monto final a pagar: ${monto_final1:.2f}")

print()  # Línea en blanco para separar los resultados

monto2 = 200.00  # Monto total de la segunda compra
porcentaje2 = 15  # Porcentaje de descuento personalizado
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2

print(f"Monto total: ${monto2:.2f}")
print(f"Descuento: ${descuento2:.2f} ({porcentaje2}%)")
print(f"Monto final a pagar: ${monto_final2:.2f}")
