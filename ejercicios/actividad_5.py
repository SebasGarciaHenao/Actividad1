# 5. Crear una función que convierta grados Fahrenheit a grados Celsius.

def grados(F,C):
    print("Uno(s)",F,"grados Fahrenheit son",C,"grados Celsius ")

gradosF=int(input("Ingrese cantidad de grados Fahrenheit: "))
gradosC=(gradosF-32)*5//9
grados(gradosF,gradosC)