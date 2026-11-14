# Ejercicio 9: Compra con descuento y cambio en pago en efectivo

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
monto_base: float = 0.0
porcentaje_descuento: float = 0.0
pago_cliente: float = 0.0
descuento: float = 0.0
total_pagar: float = 0.0
cambio: float = 0.0
valido: bool = False

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
monto_base = float(input("Monto base de la compra (S/): "))
porcentaje_descuento = float(input("Porcentaje de descuento (0-100): "))

descuento = monto_base * porcentaje_descuento / 100
total_pagar = monto_base - descuento
print(f"Total a pagar: S/ {total_pagar:.2f}")

while not valido:
    pago_cliente = float(input("¿Con cuánto dinero paga el cliente? (S/): "))
    if pago_cliente >= total_pagar:
        valido = True
    else:
        print("Error: el dinero entregado no alcanza para cubrir el total.")

# ==============================
# 3. PROCESO
# ==============================
cambio = pago_cliente - total_pagar

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nDescuento aplicado: S/ {descuento:.2f}")
print(f"Total a pagar: S/ {total_pagar:.2f}")
print(f"Cambio a recibir: S/ {cambio:.2f}")
