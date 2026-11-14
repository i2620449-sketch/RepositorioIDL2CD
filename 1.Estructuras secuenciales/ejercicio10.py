# Ejercicio 10: Cajero automático con la menor cantidad de billetes/monedas
# Denominaciones: 200, 100, 50, 20, 10, 5, 1

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
denominaciones: list = [200, 100, 50, 20, 10, 5, 1]
monto: int = 0
restante: int = 0
cantidad: int = 0
total_piezas: int = 0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
monto = int(input("Cantidad a retirar (S/, entero): "))

# ==============================
# 3. PROCESO Y 4. SALIDA DE DATOS
# ==============================
restante = monto
print(f"\nPara retirar S/ {monto} el cajero entrega:")
for valor in denominaciones:
    cantidad = restante // valor
    if cantidad > 0:
        print(f"{cantidad} x S/ {valor}")
        total_piezas += cantidad
    restante = restante % valor

print(f"Total de billetes/monedas: {total_piezas}")
