#!/usr/bin/python3
# Autor: Raul Gomez
#
# TIP: Podemos usar la funcion ZIP para iterar en dos listas al mismo tiempo
#

from pprint import pprint # para imprimir tabla
import json # para dar formato a lista de diccionarios

# -----------------------------------------------------------------------------------

print('''
---------------------------------
 Ejemplo 1
 Iterar en dos listas simples
---------------------------------
'''
)

# 1)

print('Creamos dos listas con el mismo numero de elementos:')
frutas = ['manzana','pera','uva','platano','naranja','ciruela']
colores = ['roja','verde','morada','amarillo','naranja','negra']
print(f'{frutas=}')
print(f'{colores=}')
print('')

print('Iteramos sobre dos listas al mismo tiempo con la funcion zip:')
for item in zip(frutas,colores):
  print(item)

# 2)

print('')
print('Eliminamos un valor de la lista colores para que las listas ya no tengan el mismo numero de elementos:')
colores.remove('negra')
print(f'{frutas=}')
print(f'{colores=}')
print('')

# 3)

print('Si las listas no son del mismo tamaño, la iteracion se trunca en el ultimo elemento comun:')
for item in zip(frutas,colores):
  print(item)
print('')
input('Presiona cualquier tecla para ir al siguiente ejemplo...')

# -----------------------------------------------------------------------------------

print('''
---------------------------------
 Ejemplo 2
 Iterar en una lista y una tabla
---------------------------------
'''
)

# 1)

print('Creamos lista de encabezados y tabla de clientes (tabla = lista de listas):')

encabezados = ['nombre','edad','telefono','email']

clientes = [
    ['Raul', '39', '1234567890', 'raul.agobe@gmail.com'],
    ['Abraham', '40', '0987654321', 'abraham@email.com'],
    ['Paco', '45', '1234512345', 'paco@email.com'],
    ['Alfred', '46', '9081726354', 'alfred@email.com'],
]

print(f'{encabezados=}')
print(f'{clientes=}')
print('')

# 2)

print('Iteramos en la lista de encabezados y en un elemento de la lista de clientes:')
for item in zip(encabezados,clientes[0]):
  print(item)
print('')

# 3)

print('Iteramos en la lista de encabezados y en todos los elementos de la tabla de clientes usando loops for anidados:')
for elemento in range(4):
    for item in zip(encabezados,clientes[elemento]):
      print(item)
    print('\n')
print('')
input('Presiona cualquier tecla para ir al siguiente ejemplo...')

# -----------------------------------------------------------------------------------

print('''
---------------------------------
 Ejemplo 3
 Un caso de uso practico y comun es utilizar la funcion zip 
 para iterar en una tabla y crear una lista de diccionarios
---------------------------------
'''
)

# 1)

print('Creamos una lista vacia para guardar los diccionarios')
lista_clientes_dict = list()
print(f'{lista_clientes_dict=}')
print('')

# 2)

print('Iteramos en la tabla clientes y usamos zip para construir un diccionario de encabezados : datos cliente')
for linea in clientes:
  dict_cliente = dict(zip(encabezados,linea))
  lista_clientes_dict.append(dict_cliente)
print(f'{lista_clientes_dict=}')
print('')

# 3)

print('Usamos el modulo de json para dar formato a la lista de diccionarios')
clientes_json = json.dumps(lista_clientes_dict,indent=4)
print(f'{clientes_json}')
print('')

# -----------------------------------------------------------------------------------