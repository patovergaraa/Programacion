# - - - - - - - - - - - - - - - - - - 
# CLASE 5: 
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
id = int(input("Escriba el ID del libro: "))
precio = float(input("Escriba el precio del libro: "))
enviogratuito = input("indique si el envio es gratuito (true/false): ")

if enviogratuito == "true": 
    enviogratuito = True
elif enviogratuito == "false":
    enviogratuito == False 
else: 
    enviogratuito = "El valor es incorrecto, debe escribir true/false"
print(f'''
            nombre: {nombre}
            id: {id}
            precio: {precio}
            envio gratuito?: {enviogratuito} 
''')
