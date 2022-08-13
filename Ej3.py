# Ejercicio 3

# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.

# Objetivo:

# Uso de bucles anidados

# El uso de colecciones
def primos(tope):
    primos_lista = []

    for numero in range(2,tope):
        verificador = True
        for i  in range(2,numero):
            if numero != i and numero % i == 0:
                verificador = False
                break
        if verificador == True:
            primos_lista.append(numero)
    
    print(primos_lista)


booleano = True
while booleano:
    N = int(input("Ingresa el número tope\n"))
    if N > 1:
        booleano = False
        primos(N)
    else: 
        print("el número debe ser superior a 1")