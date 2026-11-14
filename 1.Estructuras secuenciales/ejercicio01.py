# Ejercicio 1: Velocidad final de un auto (v = v0 + a*t)
# Datos del problema: v0 = 0 km/h, a = 0.8 m/s2, t = 30 s

# ==============================
# 1. DECLARACIÓN DE VARIABLES
# ==============================
velocidad_inicial_kmh: float = 0.0
velocidad_inicial_ms: float = 0.0
aceleracion: float = 0.0
tiempo: float = 0.0
velocidad_final_ms: float = 0.0
velocidad_final_kmh: float = 0.0

# ==============================
# 2. ENTRADA DE DATOS
# ==============================
velocidad_inicial_kmh = float(input("Velocidad inicial (km/h): "))
aceleracion = float(input("Aceleración (m/s2): "))
tiempo = float(input("Tiempo (s): "))

# ==============================
# 3. PROCESO
# ==============================
velocidad_inicial_ms = velocidad_inicial_kmh / 3.6          # km/h -> m/s
velocidad_final_ms = velocidad_inicial_ms + aceleracion * tiempo
velocidad_final_kmh = velocidad_final_ms * 3.6              # m/s -> km/h

# ==============================
# 4. SALIDA DE DATOS
# ==============================
print(f"\nVelocidad final: {velocidad_final_ms:.2f} m/s")
print(f"Velocidad final: {velocidad_final_kmh:.2f} km/h")
