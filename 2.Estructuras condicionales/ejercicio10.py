# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
zona = {}
codigo int = 0
minutos int = 0
nombre = ''
costo_min float= 0.0
total float= 0.0
zonas = {
    10: ('america del norte', 2.2),
    12: ('america del centro', 2.5),
    20: ('america del sur', 1.2),
    22: ('asia', 3.5),
    30: ('europa', 3.0),
    32: ('africa', 3.2),
}
codigo = int(input('ingrese el codigo de zona: '))
minutos = int(input('ingrese los minutos hablados: '))
# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
if codigo in zonas:
    nombre, costo_min = zonas [codigo]
    total = minutos * costo_min
   
# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
if codigo in zonas:
    print(f'zona: {nombre}')
    print(f'costo total: s/{total:.2f}')
else:
    print('codigo de zona no valido.')
    
