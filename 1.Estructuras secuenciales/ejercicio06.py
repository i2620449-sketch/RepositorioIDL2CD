# Ejercicio 6: Meses, semanas, días y horas aproximados vividos según la edad
# Aproximación: 1 año = 12 meses = 52 semanas = 365 días

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
edad: int = 0
meses: int = 0
semanas: int = 0
dias: int = 0
horas: int = 0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
edad = int(input("Ingrese su edad (años): "))

# ==============================
# 3. PROCESO
# ==============================
meses = edad * 12
semanas = edad * 52
dias = edad * 365
horas = dias * 24

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nCon {edad} años ha vivido aproximadamente:")
print(f"Meses:   {meses:,}")
print(f"Semanas: {semanas:,}")
print(f"Días:    {dias:,}")
print(f"Horas:   {horas:,}")
