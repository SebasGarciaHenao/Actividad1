# 10. Escribir una función que calcule el factorial de un número dado.

def factorial(n):
    if n==0:
        return 1
    else:
        
        return n*factorial(n-1)
n=int(input("Ingrese un número: "))
print("El número en factorial es: ")
print(factorial(n))