#AÑO BISIESTO

opcion = 1

while opcion == 1:
    num = int(input("Ingrese el año: "))

    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        print("El año es Bisiesto")
    else:
        print("El año no es Bisiesto")

    opcion = int(input("Para seguir adelante digite la opción 1: "))

print("Fin del proceso")