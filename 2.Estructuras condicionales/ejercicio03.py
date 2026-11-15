# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
edad int = 0
ingreso float = 0.0
tributar float = 0.0
edad = int(input('ingrese su edad: '))
Ingreso = float(input('Ingrese su ingresos mensuales (s/): '))
# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
if edad > 18 and ingreso >= 3000:
    tributar = ingreso * 0.05
# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
if edad > 18 and Ingreso >= 3000:
  
    print (f' tienes que tributar. monto: s/{tributar}')
else:
    print('No tienes que tributar.') 
