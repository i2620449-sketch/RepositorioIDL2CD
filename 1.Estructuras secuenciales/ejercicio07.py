# Ejercicio 7: Cobro de estacionamiento (S/5.00 por hora + S/0.10 por minuto restante)

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
PAGO_HORA: float = 5.00
PAGO_MINUTO: float = 0.10
horas: int = 0
minutos: int = 0
cobro: float = 0.0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
horas = int(input("Horas de estacionamiento: "))
minutos = int(input("Minutos restantes (0-59): "))

# ==============================
# 3. PROCESO
# ==============================
cobro = horas * PAGO_HORA + minutos * PAGO_MINUTO

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nTiempo: {horas} h {minutos} min")
print(f"Total a pagar: S/ {cobro:.2f}")
