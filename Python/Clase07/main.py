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
    
