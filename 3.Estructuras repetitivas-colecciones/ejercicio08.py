# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
total int = 0
hombres int = 0
suma_m int = 0
suma_h int = 0
menor int = 999
mayor int = -1
continuar str = 's'
edad int = 0
sexo int = ''

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
while continuar == 's'
edad = int(input('edad: '))
sexo = input('sexo (h/m): ')
total += 1

if edad < menor:
  menor = edad
  if edad > mayor:
    mayor = edad

if sexo == 'h'
hombres += 1
suma_h += edad
else:
suma_m += edad
continuar = input('continuar? (s/n): ')

mujeres = total - hombres
prom_h = suma_h / hombres if hombres> 0 else 0
prom_m = suma_m / mujeres if mujeres > 0 else 0

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f'total: {total}  |  hombres: {hombres}  | mujeres: {mujeres}')
print(f'promedio h: {prom_h}) | promedio m: {prom_m}')
print(f'menor edad:{menor}  |  mayor edad: {mayor}')
