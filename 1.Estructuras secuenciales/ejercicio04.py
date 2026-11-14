# Ejercicio 4: Sueldo base + 25% de comisión sobre tres ventas del mes

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
PORCENTAJE_COMISION: float = 0.25
sueldo_base: float = 0.0
venta1: float = 0.0
venta2: float = 0.0
venta3: float = 0.0
total_ventas: float = 0.0
comision: float = 0.0
sueldo_total: float = 0.0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
sueldo_base = float(input("Sueldo base (S/): "))
venta1 = float(input("Monto de la venta 1 (S/): "))
venta2 = float(input("Monto de la venta 2 (S/): "))
venta3 = float(input("Monto de la venta 3 (S/): "))

# ==============================
# 3. PROCESO
# ==============================
total_ventas = venta1 + venta2 + venta3
comision = total_ventas * PORCENTAJE_COMISION
sueldo_total = sueldo_base + comision

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nTotal de ventas: S/ {total_ventas:.2f}")
print(f"Comisión (25%): S/ {comision:.2f}")
print(f"Total a recibir en el mes: S/ {sueldo_total:.2f}")
