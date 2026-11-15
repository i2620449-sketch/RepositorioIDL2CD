# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
cantidad int = 0
precio float = 0.0
totl float = 0.0
desc float = 0.0
cantidad = int(input('ingrese la cantidad de camisas: '))
precio = float(input('ingrese el precio unitario: '))

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
totl = cantidad * precio
if cantidad <= 4:
    desc = totl * 0.125
elif cantidad <= 8:
    desc = totl * 0.20
else:
    desc = totl * 0.315

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f'sin descuento: s/{totl:.2f}')
print(f'descuento: s/{desc:.2f}')
print(f'con descuento: s/{totl - desc:.2f}')
