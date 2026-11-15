# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================

lista_valores: list = []
N: int = 0
maximo: float = 0.0
minimo: float = 0.0

# Validar la dimensión del array/lista
while True:
    try:
        N = int(input("Ingrese la cantidad de elementos de la lista: "))
        if N > 0:
            break
        print("⚠️ La cantidad debe ser superior a cero.")
    except ValueError:
        print("⚠️ Entrada inválida, digite un entero.")

# Llenado de la lista
print(f"Ingrese los {N} números de la lista:")
for i in range(1, N + 1):
    while True:
        try:
            valor: float = float(input(f" Elemento [{i}]: "))
            lista_valores.append(valor)
            break
        except ValueError:
            print("  ⚠️ Valor no válido. Intente otra vez.")

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================

maximo = lista_valores[0]
minimo = lista_valores[0]

for idx in range(1, len(lista_valores)):
    elemento_actual: float = lista_valores[idx]
    if elemento_actual > maximo:
        maximo = elemento_actual
    if elemento_actual < minimo:
        minimo = elemento_actual

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print("\n================ MÁXIMOS Y MÍNIMOS ================")
print(f"Elementos de la lista: {lista_valores}")
print(f"👉 Valor Máximo encontrado: {maximo}")
print(f"👉 Valor Mínimo encontrado: {minimo}")
print("====================================================")
