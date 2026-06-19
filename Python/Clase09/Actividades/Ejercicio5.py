#CALCULAR LA FACTORIA DE UN NUMERO

num = int(input("Digite un número: "))

while num < 0:
    num = int(input("Error. Digite un número mayor o igual a 0: "))

i = 1
factorial = 1

while i <= num:
    factorial = factorial * i
    i = i + 1

print("El factorial es:", factorial)