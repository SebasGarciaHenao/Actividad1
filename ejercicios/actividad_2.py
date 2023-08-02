# 2. Escribir una función que calcule el área de un círculo dado su radio.
def area_circulo(radio,pi,area):
    
   print("El radio del circulo es: ",radio,"su pi es: ",pi,"Y su area total es de: ",area)

radio=int(input("Ingrese el radio: "))**2

pi=float(3.1416)
area=pi*radio

area_circulo(radio,pi,area)