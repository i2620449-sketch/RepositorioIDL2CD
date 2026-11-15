# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
cantidad int = 0
precio float = 0.0
total float = 0.0
cantidad = int(input('Ingrese el numero de llantas a comprar: '))
# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
if cantidad < 5:
    precio = 150
else:
    precio = 120

total = cantidad * precio
# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f'total a pagar es: s/{total}')   
