# - - - - - - - - - - - - - - - - - - 
# CLASE 6: Sentencias de Control
# - - - - - - - - - - - - - - - - - - 

#SENTENCIA IF/ELSE#
condicion = False
if condicion:
    print("Condicion Verdera")
else: 
    print("condicion Falsa")


#CONVERSION DE NUMERO A TEXTO
num = int(input("Escriba un número en el rango del 1 al 3: "))
numtexto = " "
if num == 1:
    numtexto = "Numero uno" 
elif num == 2:
    numtexto = "Numero dos" 
elif num == 3:
    numtexto = "Numero tres" 
else: 
    numtexto = "Has ingresado un numero fuera de rango"
print(f"El numero ingresado es: {num} - {numtexto}")

#EJERCICIO 1
a = float(input("Escriba el valor de a: "))
b = float(input("Escriba el valor de b: "))
c = float(input("Escriba el valor de c: "))
resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
print (f"El resultado es: {resultado}")

#OPERADOR TERNARIO
condicion = False 
# if condicion:
# print("Condicion verdadera")
# else: 
# print("Condicion falsa")
print("Condicion Verdadera") if condicion else print("Condicion falsa")