# 3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
from random import randint

def lista_aleatoria(lista):
     lista=[randint(1,10) for i in range(0,10)]
     print(lista)

lista=print("La lista generada es: ")
lista_aleatoria(lista)
