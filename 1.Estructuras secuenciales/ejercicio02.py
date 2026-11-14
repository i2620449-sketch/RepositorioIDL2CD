# Ejercicio 2: Promedio de cuatro exámenes con la misma ponderación

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
promedio: float = 0.0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
nota1 = float(input("Nota del examen 1: "))
nota2 = float(input("Nota del examen 2: "))
nota3 = float(input("Nota del examen 3: "))
nota4 = float(input("Nota del examen 4: "))

# ==============================
# 3. PROCESO
# ==============================
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nEl promedio es: {promedio:.2f}")
