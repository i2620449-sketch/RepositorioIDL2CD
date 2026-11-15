# ==============================
# 1. ENTRADA DE DATOS / DECLARACIÓN
# ==============================

ahorro_acumulado: float = 0.0
deposito_mensual: float = 0.0
MESES_ANUAL: int = 12
meses: list = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# ==============================
# 2. PROCESO / LÓGICA Y ESTRUCTURAS
# ==============================

print("--- Registro de Ahorros Mensuales del Año ---")
for i in range(MESES_ANUAL):
    nombre_mes: str = meses[i]
    while True:
        try:
            deposito_mensual = float(input(f"Ingrese el depósito para el mes de {nombre_mes} (S/.): "))
            if deposito_mensual >= 0:
                break
            print("⚠️ El monto del depósito no puede ser negativo.")
        except ValueError:
            print("⚠️ Ingrese un valor numérico válido.")
            
    ahorro_acumulado += deposito_mensual
    print(f"   💼 Acumulado hasta {nombre_mes}: S/. {ahorro_acumulado:.2f}\n")

# ==============================
# 3. SALIDA DE RESULTADOS
# ==============================
print("================ RESUMEN DE AHORRO ANUAL ================")
print(f"💰 El ahorro total final alcanzado en el año es: S/. {ahorro_acumulado:.2f}")
print("==========================================================")
