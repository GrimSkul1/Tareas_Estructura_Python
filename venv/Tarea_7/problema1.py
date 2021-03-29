# Nombre del problema: Ice Cream Parlor

#|Descripcion: Dada una lista de precios para los sabores de helado, seleccionar dos que costarian todo el dinero que tienen
#   Ejemplo: m = 6 costo = [1,3,4,5,6]
#
#   los dos sabores que cuestan 1 y 5 cumplen los criterios. usando 1 indexado basado en los indices 1 y 4.
#
#   Funcion a utilizar:
#   Complete la funcion icecreamParlor con los siguientes parametros:
#   - int m: la cantidad de dinero que tiene que gastar
#   - int cost[n]: el costo de cada sabor de helado
#
#   Debe retornar:
#   int[2]: los indices de los precios de los dos sabores que compran, ordenadaos de forma ascendete.
#
#   Se deben tener algunas restricciones pendientes
#   - 1 ≤ t ≤ 50
#   - 2 ≤ m ≤ 10^4
#   - 2 ≤ n ≤ 10^4
#   -1 ≤ cost[i] ≤ 10^4, ∀ i Ɛ [1,n] |#

import math
import os
import random
import re
import sys


#el codigo tiene un tiempo de corrida de O(n)

def icecreamParlor(m,arr):
    test = dict() # se inicializa un diccionario
    for i in range(len(arr)): # se corre un for por la longitud del arreglo de precios
        if arr[i] not in test: # se comprara si el arreglo de precios dados no se encuentra en el diccionario
            #se iguala el diccionario
            # se le aumenta 1 para que retorne el contenido exacto de dinero
            test[m-arr[i]] = i+1
        else:
            # se organiza el arreglo de menor a mayor
            return sorted([i+1, test[arr[i]]])


arreglo = [1,3,4,5,6]
dinero = 6
resultado = icecreamParlor(dinero,arreglo)

print(resultado)