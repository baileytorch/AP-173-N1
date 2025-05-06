from ejercicios.ejercicio_1 import convertidor_temp

temp = float(input("Ingrese su temperatura a convertir: "))
escala_inicial = input("Indique escala inicial: C, F o K: ").upper().strip()
escala_final = input("Indique escala final: C, F o K: ").upper().strip()

convertidor_temp(temp,escala_inicial,escala_final)