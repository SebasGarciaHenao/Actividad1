# 8. Crear una función que invierta el orden de los elementos en una lista dada.
lista=[1,2,3,4,5,6,7,8,9,10]

def invertir_lista(listanormal,listainvertida):
    print("la lista normal es: ",listanormal)
    print("la lista invertida es: ",listainvertida)

listaNormal=lista
listaInvertida=lista[::-1]
invertir_lista(listaNormal,listaInvertida)
    
    