# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
n1 int = 0
n2 int = 0
n3 int = 0
orden string = ''
lista = []
n1 = int(input('ingrese el primer numero: '))
n2 = int(input('ingrese el segundo numero: '))
n3 = int(input('ingrese el tercer numero: '))

orden = input('desea ordenar de forma ascendente o descentente?: ').strip().lower()

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
lista = sorted({n1,n2,n3}, reverse= (orden == 'descendente'))

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print('numeros ordenados:', lista)
