#!/usr/bin/python3
# Autor: Raul Gomez
#
# TIP: Podemos usar la funcion ZIP para iterar en dos listas al mismo tiempo
#


# -------------------------------
# Ejemplo 1
# Iterar en dos listas simples
# -------------------------------

# Creamos dos listas con el mismo numero de elementos

frutas = ['manzana','pera','uva','platano','naranja','ciruela']
colores = ['roja','verde','morada','amarillo','naranja','negra']

# iteramos sobre dos listas al mismo tiempo

for f,c in zip(frutas,colores):
  print(f,'-',c)

# Eliminamos un valor de la lista colores para que las listas ya no tengan el mismo numero de elementos

colores.remove('negra')
print(frutas)
print(colores)

# Si las listas no son del mismo tamaño, la iteracion se trunca en el ultimo elemento comun

for f,c in zip(frutas,colores):
  print(f,'-',c)

# -------------------------------
# Ejemplo 2
# Iterar en una lista y una tabla
# -------------------------------

# Creamos lista de encabezados y tabla de clientes (tabla = lista de listas)

encabezados = ['nombre','edad','telefono','email']

clientes = [
    ['raul', '39', '1234567890', 'raul.agobe@gmail.com'],
    ['maria', '68', '0987654321', 'maria@email.com'],
    ['juan', '25', '1234512345', 'juan@email.com'],
    ['ramiro', '19', '918762354', 'ramiro@email.com'],
]

# Iteramos en la lista de encabezados y en un elemento de la lista de clientes

for e,c in zip(encabezados,clientes[0]):
  print(e,'-',c)

# Iteramos en la lista de encabezados y en todos los elementos de la tabla de clientes usando loops for anidados

for elemento in range(4):
    for e,c in zip(encabezados,clientes[elemento]):
      print(e,'-',c)
    print('\n')


# Un caso de uso practico y comun es utilizar la funcion zip para iterar en una tabla y crear una lista de diccionarios

lista_clientes_dict = list()

for linea in clientes:
  dict_clientes = dict(zip(encabezados,linea))
  lista_clientes_dict.append(dict_clientes)


# Usamos el modulo de json para dar formato a la lista de diccionarios

import json

clientes_json = json.dumps(lista_clientes_dict,indent=4)
print(clientes_json)
