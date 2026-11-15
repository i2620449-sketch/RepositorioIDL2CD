# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
minutos int = 0
subtotal float = 0.0
minutos = int(input('ingrese la duracion en minutos: '))
# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
subtotal = sum(1.0 if i <= 5 else (0.8 if i <= 8 else (0.7 if i <= 10 else 0.5)) for i in range(1, minutos + 1))

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f'subtotal: s/ {subtotal:.2f}')
