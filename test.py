# from ejercicios.ejercicio_1 import convertidor_temp

# temp = float(input("Ingrese su temperatura a convertir: "))
# escala_inicial = input("Indique escala inicial: C, F o K: ").upper().strip()
# escala_final = input("Indique escala final: C, F o K: ").upper().strip()

# convertidor_temp(temp,escala_inicial,escala_final)
# lista_comidas = ['sopaipillas','charquican','empanadas']
# print(lista_comidas[2])
# lista_comidas[2] = 'Empanadas fritas'
# print(lista_comidas)
# for i in range(5):
#     print(i)

# def division(a,b):
#     resultado = a/b
#     return resultado

# numero1_str = input('Ingrese número:')
# numero2_str = input('Ingrese número:')
# numero1 = 0
# numero2 = 0

# if numero1_str.isdigit():
#     numero1 = int(numero1_str)
# if numero2_str.isdigit():
#     numero2 = int(numero2_str)

# division(numero1,numero2)

# cadena_test = '''
# Mi corazón, ni una ni dos veces se rompió.
# Sus bolsillos se vaciaron por las necesidades de ambos.
# Un control lo suficientemente fuerte no podría contener sus finanzas.
# Sobre la dignidad o la luz que una vez hubo en mi alma
# Desde la primera compra mi corazón no aprendió
# Tomó prestado de otros lugares para poder ganar dinero.
# El precio que pediste a cambio por tu amor.
# El precio que pediste a cambio por tu amor.
# Mi corazón, ni una ni dos veces se rompió.
# En quiebra, agotados, sólo entonces para tomar nota
# Que por error había utilizado mala economía
# En la compra del amor, que debería haber venido gratis
# '''
try:
    valor = int(input('ingrese un entero: '))
    print(valor)
except:
    print('Valor incorrecto')
