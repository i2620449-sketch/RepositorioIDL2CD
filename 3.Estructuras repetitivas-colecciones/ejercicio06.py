# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================
horas int = 0
minutos int = 0
segundos int = 0
cronometro str = ''

horas = int(input('ingrese las horas: '))
minutos = int(input('ingrese los minutos: '))
segundos = int(input('ingrese los segundos: '))

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================
cronometro = (f'{str(horas).zfill(2)}:{str(str(minutos).zfill(2)}:{tr(minutos).zfill(2)}:{str(segundos).zfill(2)}')

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print(f'tiempo registrado: {cronometro}')
