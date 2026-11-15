# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
materias int = 0
promedio float = 0
total_de_costo float = 0.0
descuento float = 0.0
materias = int(input('ingrese la cantidad de materias que cursa: '))
promedio = float(input('ingrese el promedio del ultimo periodo: '))
# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
total_de_costo = meterias * 100
if promedio >= 18:
  descuento = (materias/ 2) * 50
  total_de_costo -= descuento
# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f' el monto total es: s/{total_de_costo}')
