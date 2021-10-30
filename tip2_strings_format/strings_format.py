#!/usr/bin/python3
# Autor: Raul Gomez
#
# TIP: Distintas formas de darle formato a un string
# 
# https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
#

# Creamos algunas variables para trabajar un frase
n = 'Raul'
a = 'Gomez'
e = '39'

# Para incorporar las variables creadas a la frase podemos concatenar fragmentos de la frase (strings) con las variables
frase = 'Hola, mi nombre es ' + n + ' ' + a + ' y tengo ' + e + ' años'
print(frase)

# En Python2 surgio la opcion de darle formato a los strings usando placeholders (%)
frase = 'Hola, mi nombre es %s %s y tengo %s años' % (n,a,e)
print(frase)

# En Python3 Los placeholders fueron reemplazados por la funcion format
frase = 'Hola, mi nombre es {} {} y tengo {} años'.format(n,a,e)
print(frase)

# Una ventaja de usar str.format() es que podemos indicar el indice de los argumentos de la funcion en los {} y cambiar el orden en el que usamos las variables
frase = 'Hola, mi nombre es {2} {0} y tengo {1} años'.format(n,a,e)
print(frase)

# A partir de Python3.6 podemos usar f-strings
frase = f'Hola, mi nombre es {n} {a} y tengo {e} años'
print(frase)

# Con f-strings puedes imprimir en la terminal el nombre de la variable usando el simbolo de =
saludo = f'Hola, soy {n=} {a=}'
print(saludo)


# Todo esto aplica tambien para strings multilinea

v = 'Raul Gomez'
d = '15'
p = 'Mexico, Colombia, Peru (Total 3)'
g = '$50,000 MXN'


reporte = '''
======================================================================
Reporte de viaje (Concatenar)
======================================================================
Viajero: ''' + v + '''
Paises visitados: ''' + p + '''
Dias de viaje: ''' + d + '''
Gastos: ''' + g + '''
======================================================================
'''
print(reporte)


reporte = '''
======================================================================
Reporte de viaje (Placeholder)
======================================================================
Viajero: %s
Paises visitados: %s
Dias totales: %s
Gastos: %s
======================================================================
''' % (v,p,d,g)
print(reporte)


reporte = '''
======================================================================
Reporte de viaje (string.format())
======================================================================
Viajero: {}
Paises visitados: {}
Dias totales: {}
Gastos: {}
======================================================================
'''.format(v,p,d,g)
print(reporte)


reporte = f'''
======================================================================
Reporte de viaje (f-strings)
======================================================================
Viajero: {v}
Paises visitados: {p}
Dias totales: {d}
Gastos: {g}
======================================================================
'''
print(reporte)
