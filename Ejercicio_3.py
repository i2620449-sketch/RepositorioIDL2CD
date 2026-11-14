#==================================================
#EJERCICIO 2 
#==================================================
"Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad"
"distinta. Obtener el porcentaje que cada uno invierte con respecto a la cantidad total invertida "
#DECLARACION EN INICIALIZACION DE VARIABLES
#ENTRADA DE DATOS DEL USUARIO
inversion_1 = float(input("Ingrese el monto invertido por la persona 1: "))
inversion_2 = float(input("Ingrese el monto invertido por la persona 2: "))
inversion_3 = float(input("Ingrese el monto invertido por la persona 3: "))


#PROCESAMIENTO DE DATOS 
total_inversion = inversion_1 + inversion_2 + inversion_3
porcentaje_1 = (inversion_1/total_inversion)*100
porcentaje_2 = (inversion_2/total_inversion)*100
porcentaje_3 = (inversion_3/total_inversion)*100
#SALIDA DE RESULTADOS
print("\n----- RESULTADOS DE LA INVERSIÓN --------")
print(f"Total invertido: S/ {total_inversion:.2f}")
print(f"Porcentaje Persona 1:{porcentaje_1:.2f} %")
print(f"Porcentaje Persona 2:{porcentaje_2:.2f} %")
print(f"Porcentaje Persona 3:{porcentaje_3:.2f} %")