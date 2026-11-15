# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================

# Declaración e inicialización de variables
N: int = 0
X: float = 0.0
lista_numeros: list = []

menores_x: int = 0
mayores_x: int = 0
iguales_x: int = 0
comprendidos_1_x: int = 0
sin_condicion: int = 0

# Validación del tamaño N de la lista
while True:
    try:
        N = int(input("Ingrese la cantidad N de números a registrar: "))
        if N > 0:
            break
        print("⚠️ La cantidad de números debe ser mayor a 0.")
    except ValueError:
        print("⚠️ Ingrese un número entero válido.")

# Solicitar el valor de referencia X
while True:
    try:
        X = float(input("Ingrese el valor de referencia X: "))
        break
    except ValueError:
        print("⚠️ Ingrese un valor numérico real para X.")

# Lectura y almacenamiento de los N números en la lista
print(f"\nProceda a ingresar los {N} números:")
for i in range(1, N + 1):
    while True:
        try:
            num: float = float(input(f"  Número {i}/{N}: "))
            lista_numeros.append(num)
            break
        except ValueError:
            print("  ⚠️ Entrada no válida. Intente nuevamente.")

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================

for num in lista_numeros:
    cumple_alguna: bool = False

    if num < X:
        menores_x += 1
        cumple_alguna = True

    if num > X:
        mayores_x += 1
        cumple_alguna = True

    if num == X:
        iguales_x += 1
        cumple_alguna = True

    if 1 <= num <= X:
        comprendidos_1_x += 1
        cumple_alguna = True

    if not cumple_alguna:
        sin_condicion += 1

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f"\n================ ANÁLISIS DE PORCENTAJES (X = {X}) ================")
print(f"Lista registrada: {lista_numeros}")
print(f"• Menores que X             : {menores_x} ({ (menores_x / N) * 100:.2f}%)")
print(f"• Mayores que X             : {mayores_x} ({ (mayores_x / N) * 100:.2f}%)")
print(f"• Iguales a X               : {iguales_x} ({ (iguales_x / N) * 100:.2f}%)")
print(f"• Comprendidos entre 1 y X  : {comprendidos_1_x} ({ (comprendidos_1_x / N) * 100:.2f}%)")
print(f"• No cumplen ninguna cond.  : {sin_condicion} ({ (sin_condicion / N) * 100:.2f}%)")
print("==================================================================")
