import funciones.cuadrilatero

def menu_principal():
    print()
    print("Cálculo de funciones geométricas.")
    print("1: Perímetro")
    print("2: Área")
    print("3: Volumen")
    print("0: Salir")
    print()
    
    while True:
        opcion = input("Seleccione su opción (0-3): ")
        
        if opcion == "1":
            ancho = input("Ingrese el ancho: ")
            largo = input("Ingrese el largo: ")
            print(funciones.cuadrilatero.perimetro(ancho,largo))
            
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "0":
            print("saliendo del sistema...")
            break
        else:
            print("Opción inválida...")

menu_principal()