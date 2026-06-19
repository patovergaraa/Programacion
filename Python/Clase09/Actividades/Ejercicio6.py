
n_elementos = int(input("Digite la cantidad de elementos a ingresar: "))

suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0

for i in range(1, n_elementos + 1):
    num = int(input(f"{i}. Digite un numero: "))

    if num % 2 == 0:
        suma_pares += num
        conteo_pares += 1
    else:
        suma_impares += num
        conteo_impares += 1

if conteo_pares > 0:
    print("La suma de los numeros pares es:", suma_pares)
    print("El conteo de los numeros pares es:", conteo_pares)
else:
    print("No se han digitado numeros pares")

if conteo_impares > 0:
    promedio_impares = suma_impares / conteo_impares
    print("El promedio de los numeros impares es:", promedio_impares)
else:
    print("No se han digitado numeros impares")