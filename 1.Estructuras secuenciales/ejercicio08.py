# Ejercicio 8: Área de un terreno de forma A (rectángulo + triángulo)
# Lados: A = lado izquierdo (alto), B = base, C = lado derecho (alto menor)
# Área = B*C + B*(A-C)/2

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
lado_a: float = 0.0
lado_b: float = 0.0
lado_c: float = 0.0
valido: bool = False
area_rectangulo: float = 0.0
area_triangulo: float = 0.0
area_total: float = 0.0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
while not valido:
    lado_a = float(input("Lado A (m): "))
    lado_b = float(input("Lado B (m): "))
    lado_c = float(input("Lado C (m): "))
    if lado_a >= lado_c:
        valido = True
    else:
        print("Error: el lado A debe ser mayor o igual que el lado C.\n")

# ==============================
# 3. PROCESO
# ==============================
area_rectangulo = lado_b * lado_c
area_triangulo = lado_b * (lado_a - lado_c) / 2
area_total = area_rectangulo + area_triangulo

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nÁrea del rectángulo: {area_rectangulo:.2f} m2")
print(f"Área del triángulo: {area_triangulo:.2f} m2")
print(f"Área total del terreno: {area_total:.2f} m2")
