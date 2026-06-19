
i = 1
suma = 0

while i <= 5:
    print("Salario del empleado", i)

    horas = float(input("Digite las horas trabajadas: "))
    tarifa = float(input("Digite la tarifa por hora: "))

    salario = horas * tarifa

    print("El salario es:", salario)

    suma = suma + salario

    i = i + 1

print("La suma de todos los salarios es:", suma)