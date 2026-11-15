# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
L1 float = 0.0
L2 float = 0.0
L3 float = 0.0
perimetro = 0.0
L1 = float(input('Ingrese el lado 1: '))
L2 = float(input('Ingrese el lado 2: '))
L3 = float(input('ingrese el lado 3: '))
# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
if L1 == L2 and L2 == L3:
    perimetro = L1 + L2 + L3
# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
if L1 == L2 and L2 == L3:
    perimetro = L1 + L2 + L3
    print(f'trinagulo equilatero. perimetro:{perimetro}')
 elif L1 == L2 or L1 == L3 or L2 == L3:
    print('triangulo isosceles.')
 else:
    print('triangulo escaleno.')
