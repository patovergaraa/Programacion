#LEER 10 NUMEROS E IMPRIMIR CUANTOS SON POSITIVOS, NEGATIVOS Y NEUTROS.

conteo_positivos = 0
conteo_negativos = 0
conteo_neutros = 0

for i in range(10):
    num = int(input("Digite un número: "))

    if num > 0:
        conteo_positivos += 1
    elif num < 0:
        conteo_negativos += 1
    else:
        conteo_neutros += 1

print("La cantidad de positivos es:", conteo_positivos)
print("La cantidad de negativos es:", conteo_negativos)
print("La cantidad de neutros es:", conteo_neutros)