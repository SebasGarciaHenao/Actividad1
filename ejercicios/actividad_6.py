# 6. Crear un programa que calcule la suma de los números en una lista dada.
lista=[1,2,3,4,5,6,7,8,9,10]

def sumas_lista(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma
print("La suma totdal de la lista es de: ",sumas_lista(lista))
   


 
