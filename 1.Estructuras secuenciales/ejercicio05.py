# Ejercicio 5: Ganancia en un año con interés de 2% mensual (interés simple)

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
TASA_MENSUAL: float = 0.02
MESES: int = 12
capital: float = 0.0
ganancia: float = 0.0
total_final: float = 0.0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
capital = float(input("Capital a invertir (S/): "))

# ==============================
# 3. PROCESO
# ==============================
ganancia = capital * TASA_MENSUAL * MESES
total_final = capital + ganancia

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nGanancia después de un año: S/ {ganancia:.2f}")
print(f"Capital final: S/ {total_final:.2f}")
