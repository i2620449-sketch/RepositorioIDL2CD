# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
n int = 0
nota int = 0 
suma  float= 0.0
mayor = -1
menor int = 21
cant_mayor int = 0
cant_menor int = 0
pares int = 0 
impares int = 0
aprobados int = 0 
desaprobados  int =  0

while n < 5 or n > 20:
  n = int(input('ingrese la cantidad de estudintes(5 a 20): '))
# ============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
for i in range(1, n + 1):
  nota = -1
  while nota < 0 or nota > 20:
    nota = int(input(f'nota del alumno{i} (0 a 20): '))
    suma += nota

if nota > mayor:
  mayor = nota
  cant_nota = 1
elif nota == mayor:
  cant_mayor += 1

if nota < menor:
  menor = nota
  cant_menor = 1
elif nota == menor:
  cant_menor += 1
  
  if nota % 2 == 0:
    pares += 1
  else:
    impares += 1
    
    if nota >= 13:
      aprobado += 1
    else:
      desaprobado += 1
promedio = suma/n
porc_aprob = (aprobados/ n) * 100
porc_desaprob = (desprobados / n) * 100
      
# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
prit(f'a) mayor nota: {mayor}')
prit(f'b) menor nota: {menor}')
prit(f'c) alumnos con mayor nota: {cant_mayor}')
prit(f'd) alumnos con menor nota: {cant_menor}')
prit(f'e) promedio del salon: {promedio}')
prit(f'f) notas pares: {pares}')
prit(f'g) notas impares: {impares}')
prit(f'h) apobados: {aprobados}')
prit(f'i) desaprobados: {desprobados}')
prit(f'j) porcentaje apobado: {porc_aprob}%')
prit(f'k) porcentaje desaprobado: {porc_desprob}%')
