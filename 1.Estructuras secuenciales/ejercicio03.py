# Ejercicio 3: Porcentaje que invierte cada socio respecto al total

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
inversion1: float = 0.0
inversion2: float = 0.0
inversion3: float = 0.0
total: float = 0.0
porcentaje1: float = 0.0
porcentaje2: float = 0.0
porcentaje3: float = 0.0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
while total == 0:
    inversion1 = float(input("Inversión de la persona 1 (S/): "))
    inversion2 = float(input("Inversión de la persona 2 (S/): "))
    inversion3 = float(input("Inversión de la persona 3 (S/): "))
    total = inversion1 + inversion2 + inversion3
    if total == 0:
        print("Error: el total invertido debe ser mayor que 0.\n")

# ==============================
# 3. PROCESO
# ==============================
porcentaje1 = inversion1 / total * 100
porcentaje2 = inversion2 / total * 100
porcentaje3 = inversion3 / total * 100

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nTotal invertido: S/ {total:.2f}")
print(f"Persona 1: {porcentaje1:.2f}%")
print(f"Persona 2: {porcentaje2:.2f}%")
print(f"Persona 3: {porcentaje3:.2f}%")
