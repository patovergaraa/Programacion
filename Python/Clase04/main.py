# - - - - - - - - - - - - - - - - - - 
# CLASE 4: 
# - - - - - - - - - - - - - - - - - - 

#OPERADORES ARIMÉTICOS
operandoA = 8 
operandoB = 5 
suma = operandoA + operandoB
#print("Resultado de la suma: ", suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

#RECTÁNGULO

alto = int(input("proporciona el alto del rectangulo: "))
ancho = int(input("proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Area: ", area)
print("perimetro: ", perimetro)


#OPERADORES DE ASIGNACIÓN Y COMPARACIÓN
miVariable3 = 10
print(miVariable3)

#REASIGNACIÓN
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

miVariable3 -= 2
print(miVariable3)

miVariable3 *= 3 
print(miVariable3)

miVariable3 /= 2
print(miVariable3)

#COMPARACION 
d = 4
b = 4

resultado = d == b #Comprobamos si son iguales
print(resultado)

#Operador diferente 
resultado = d != b
print(resultado)

#Operador mayor que
resultado = d > b 
print(resultado)

#Operador menor que
resultado = d < b 
print(resultado) 

#Operador menor o igual que 
resultado = d <= b 
print(resultado)



#EJERCICIO1 
a = int(input("Escriba un número: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un numero PAR")
else:
    print(f"El valor de a es: {a} es un numero IMPAR")



#EJERCICIO2
edadAdulto = 18
edadpersona = int(input("Escriba su edad: "))
if edadpersona >= edadAdulto:
    print(f"Su edad es: {edadAdulto}, es mayor de edad")
else: 
    print(f"Su edad es: {edadpersona}, es menor de edad")