# 7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

import heapq

lista=[54,1,4,88,465,32032,5,78,8]

def lista_mayor_menor(lista):
    print("El número mas grande de la lista es:" ,heapq.nlargest(1,lista))
    print("El número mas pequeño de la lista es:" ,heapq.nsmallest(1,lista))
lista
lista_mayor_menor(lista)