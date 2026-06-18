print ("¿Cómo estuvo tu día? (Del 1 al 10)")
dia = int(input())

if 1<=dia<=10:
    print("Mi día estuvo de:", dia)

else:
    print("Inválido, debe ingresar un número entre 1 y 10")