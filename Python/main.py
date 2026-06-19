# - - - - - - - - - - - - - - - - - - 
# CLASE 2: Variables en Python
# - - - - - - - - - - - - - - - - - - 

miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben x528, la variable y = x272, la variable z = x592
print(id(y))
print(id(z))

# - - - - - - - - - - - - - - - - - - 
# CLASE 3: Tipos de datos en Python
# - - - - - - - - - - - - - - - - - - 

#Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "The Letter Black: "
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tpos Boleanos (boot)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion input
resultado = input("Digite un numero: ") # Regresa un dato tipo string
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

# - - - - - - - - - - - - - - - - - - 
# CLASE 4: Operadores en Python Parte 1
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

# - - - - - - - - - - - - - - - - - - 
# CLASE 5: Operadores en Python Parte 2
# - - - - - - - - - - - - - - - - - - 

#OPERADORES LOGICOS (and-or:binarios(dos numeros) / not:no binario(un numero))

a = False
b = True
resultado = a and b 
print(resultado)

#OR

resultado = a or b 
print(resultado)

#NOT 

resultado = not a 
print(resultado)

#VALOR DENTRO DE UN RANGO

valor = int(input("Escriba un numero dentro del rango 0 al 5: "))
valorminimo = 0
valormaximo = 5 
dentrorango = (valor >= valorminimo and valor <= valormaximo)

if dentrorango:
    print(f"El valor {valor} esta dentro del rango")
else: 
    print (f"El valor {valor} no esta dentro del rango")



#EJERCICIO CON OR 

vacaciones = False 
diadedescanso = False
if vacaciones or diadedescanso:
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")

#EJERCICIO: RANGO ENTRE 20 Y 30 AÑOS

edad = int(input("Escriba su edad: "))
veinte = edad >= 20 and edad <30
print(veinte)
treinta = edad >= 30 and edad < 40 
print(treinta)

if veinte or treinta: 
    print("Estas dentro del rango de los (20\"0) a (30\"0) años")
else: 
    print("No estas dentro del rango de los (20\"0) a (30\"0) años")



#EJERCICIO1: EL MAYOR DE DOS NUMEROS

numero1 = int(input("Escriba el valor para el numero 1: "))
numero2 = int(input("Escriba el valor para el numero 2: "))

if numero1 > numero2:
    print("El numero 1 es mayor")
else: 
    print("El numero 2 es mayor")


#EJERCICIO: TIENDA DE LIBROS 
print("Escriba los siguientes datos del libro")
nombre = input("Escriba el nombre del libro: ")
id_libro = int(input("Escriba el ID del libro: "))
precio = float(input("Escriba el precio del libro: "))
enviogratuito = input("indique si el envio es gratuito (true/false): ")

if enviogratuito == "true": 
    enviogratuito = True
elif enviogratuito == "false":
    enviogratuito = False 
else: 
    enviogratuito = "El valor es incorrecto, debe escribir true/false"
print(f'''
            nombre: {nombre}
            id: {id}
            precio: {precio}
            envio gratuito?: {enviogratuito} 
''')

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
#print("Condicion Verdadera") if condicion else print("Condicion falsa")

# - - - - - - - - - - - - - - - - - - 
# CLASE 7: Ciclo While y for
# - - - - - - - - - - - - - - - - - - 

#CICLO WHILE (MIENTRAS O DURANTE)

contador = 0 

while contador < 3:
    print("Ejecutamos nuestro ciclo while", contador)
    contador += 1
#else: 
    print("Fin del ciclo while")

#IMPRIMIR NUMEROS DEL 0 AL 5 CON EL CICLO WHILE

maximo = 5 
contador = 0 
while contador <= maximo: 
    print(contador)
    contador += 1 

minimo = 1 
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1

#CICLO FOR 

cadena = "Hola"
for letra in cadena:
    print(letra)
#else: 
    print("Fin del ciclo for")

#PALABRA RESERVADA BREAK 

for letra in "ARGENTINA":
    if letra == "A":
        print(f"Letra encontrada : {letra}")
        break
else: 
    print("Fin del ciclo for")

#PALABRA RESERVADA CONTINUE

for i in range(6): 
    if i % 2 == 0:
        print(f"valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue 
    print (f"valor: {i}")
    
# - - - - - - - - - - - - - - - - - - 
# CLASE 8: Ejercicios y Mucha práctica
# - - - - - - - - - - - - - - - - - - 

# - - - - - - - - - - - - - - - - - - 
# CLASE 9: Ejercicios en Python grupal
# - - - - - - - - - - - - - - - - - - 