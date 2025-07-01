cadena = 'esta es una variable de tipo string'

print(type(cadena))
# print(dir(cadena))

# 'capitalize' Pone en mayúsculas la primera letra del texto
print(cadena.capitalize())

# 'casefold'
# 'center'

# 'count' Cuenta la cantidad de caracteres buscado dentro de un string
print(cadena.count('es'))
# 'encode'

# 'endswith' Devuelve V si la cadena termina en una búsqueda específica
print(cadena.endswith('ing'))
print(cadena.endswith('t'))

# 'expandtabs'

# 'find' Devuelve el índice de la posición si se encuentra el texto buscado dentro de una cadena
# o devuelve -1 si no encuentra el substring
print(cadena.find('juenito'))
print(cadena.find('es'))

# 'format'
# 'format_map'
# 'index' Similar a find()
# 'isalnum'
# 'isalpha'
# 'isascii'
# 'isdecimal'
# 'isdigit'
# 'isidentifier'
# 'islower'
if cadena.islower():
    print('el string tiene sólo letras minúsculas')
else:
    print('el string NO tiene sólo letras minúsculas')
# 'isnumeric'
# 'isprintable'
# 'isspace'
# 'istitle'
# 'isupper'
# 'join'
# 'ljust'
# 'lower'
# 'lstrip'
# 'maketrans'
# 'partition'
# 'removeprefix'
# 'removesuffix'
# 'replace'
# 'rfind'
# 'rindex'
# 'rjust'
# 'rpartition'
# 'rsplit'
# 'rstrip'
# 'split'
cadena_split = cadena.split(' ')
print(cadena_split)

# 'splitlines'
# 'startswith'
# 'strip'
# 'swapcase'
# 'title'
# 'translate'
# 'upper'
print(cadena.upper())
# 'zfill'