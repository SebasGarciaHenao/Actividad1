# 4. Escribir un programa que determine si un número dado es par o impar.

def par_impar(numero):
    if numero%2==0:
        print("El número es par:")
    else:
        print("El numero es impar")
numero=int(input("Ingrese un número: "))
par_impar(numero)