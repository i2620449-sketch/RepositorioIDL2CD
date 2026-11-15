# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================

# Declaración e inicialización de variables con tipado estático (Type Hints)
N: int = 0
suma_pares: int = 0
suma_impares: int = 0
cant_pares: int = 0
cant_impares: int = 0
promedio_pares: float = 0.0
promedio_impares: float = 0.0

# Solicitud de datos al usuario con validación para asegurar un número positivo
while True:
    try:
        N = int(input("Ingrese un número entero positivo N: "))
        if N > 0:
            break
        else:
            print("⚠️ Por favor, ingrese un número mayor a cero.")
    except ValueError:
        print("⚠️ Entrada no válida. Debe ingresar un número entero.")

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================

# Bucle desde 1 hasta N inclusive para evaluar cada número
for i in range(1, N + 1):
    # Estructura condicional para determinar si el número es par
    if i % 2 == 0:
        suma_pares += i       # Acumula la suma de pares
        cant_pares += 1       # Incrementa el contador de pares
    else:
        suma_impares += i     # Acumula la suma de impares
        cant_impares += 1     # Incrementa el contador de impares

# Cálculo de promedios controlando la división por cero
if cant_pares > 0:
    promedio_pares = suma_pares / cant_pares

if cant_impares > 0:
    promedio_impares = suma_impares / cant_impares

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print("\n================ RESULTADOS ================")
print(f"Rango evaluado: 1 hasta {N}")
print(f"• Números Pares detectados: {cant_pares}")
print(f"  -> Suma total: {suma_pares}")
print(f"  -> Promedio: {promedio_pares:.2f}")
print(f"• Números Impares detectados: {cant_impares}")
print(f"  -> Suma total: {suma_impares}")
print(f"  -> Promedio: {promedio_impares:.2f}")
print("============================================")
