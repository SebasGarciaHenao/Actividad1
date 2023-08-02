# 1.Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.

def nombre_edad(nombre,edad):
    print("Su nombre es ",nombre, "y su edad es de ",edad,"años")
  
nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")
nombre_edad(nombre,edad)