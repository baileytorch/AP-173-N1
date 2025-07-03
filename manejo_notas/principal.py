from data.conexion import ejecutar_consulta
from prettytable import PrettyTable

# READ
def menu_principal():
    script_sql = '''
        SELECT numero_opcion,opcion_menu 
        FROM opciones_menu
        WHERE tipo_menu = 1
    '''
    print()
    print('SISTEMA DE GESTIÓN ASIGNATURAS')
    opciones_menu = ejecutar_consulta(script_sql)
    tabla_menu = PrettyTable()
    tabla_menu.field_names = ['Id','Opción']
    for asignatura in opciones_menu:
        tabla_menu.add_row(asignatura) # type: ignore
    print(tabla_menu)
    opcion_usuario = input(f'Seleccione su opción [0-{len(opciones_menu)-1}] :')

menu_principal()