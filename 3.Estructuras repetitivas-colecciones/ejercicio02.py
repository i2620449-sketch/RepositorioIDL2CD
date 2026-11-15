# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================

# Declaración de variables y contadores con tipado explícito
numero: float = 0.0
pares: int = 0
impares: int = 0
positivos: int = 0
negativos: int = 0
neutros: int = 0
TOTAL_NUMEROS: int = 10

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================

print(f"Por favor, ingrese {TOTAL_NUMEROS} números:")

# Estructura repetitiva determinada para solicitar exactamente 10 números
for i in range(1, TOTAL_NUMEROS + 1):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i}/{TOTAL_NUMEROS}: "))
            break
        except ValueError:
            print("⚠️ Entrada inválida. Ingrese un valor numérico real o entero.")

    # Evaluación de signo (Positivo, Negativo o Neutro)
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        neutros += 1

    # Evaluación de paridad
    if int(numero) % 2 == 0:
        pares += 1
    else:
        impares += 1

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print("\n================ CLASIFICACIÓN DE NÚMEROS ================")
print(f"Total de números analizados: {TOTAL_NUMEROS}")
print(f"• Positivos : {positivos}")
print(f"• Negativos : {negativos}")
print(f"• Neutros (0): {neutros}")
print(f"• Pares     : {pares} (según parte entera)")
print(f"• Impares   : {impares} (según parte entera)")
print("===========================================================")
