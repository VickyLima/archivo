import os
os.system('cls')

# EJERCICIO
'''
Escribe un programa en Python que permita leer un grupo variable de números enteros positivos utilizando 
un ciclo While. También debe hacer que obtenga la suma total, el máyor, el menor y el promedio, así 
como el numero de valores que pertenecen a las unidades, a las decenas, a las centenas o a los millares. 
'''
def menu():
    print("Menú de opciones:")
    print("1. Mostrar suma total")
    print("2. Mostrar número mayor")
    print("3. Mostrar número menor")
    print("4. Mostrar promedio")
    print("5. Mostrar distribución por unidades, decenas, centenas y millares")
    print("0. Salir")
    print("-" * 40)

# Inicializar variables
numeros = []
suma = 0
mayor = 0
menor = None
numero_unidades = 0
numero_decenas = 0
numero_centenas = 0
numero_millares = 0

# Leer cantidad de números
cant_numeros = int(input("¿Cuántos números desea ingresar?: "))

# Leer números
for i in range(cant_numeros):
    numero = int(input("Introduzca un número entero positivo: "))
    numeros.append(numero)
    
    # Actualizar variables
    suma += numero
    if mayor < numero:
        mayor = numero
    if menor is None or numero < menor:
        menor = numero
    
    # Contar por unidades, decenas, centenas y millares
    if numero < 10:
        numero_unidades += 1
    elif numero < 100:
        numero_decenas += 1
    elif numero < 1000:
        numero_centenas += 1
    else:
        numero_millares += 1

# Calcular el promedio
promedio = suma / len(numeros)

# Mostrar menú y obtener opción
opcion = -1
while opcion != 0:
    menu()
    opcion = int(input("Introduzca una opción: "))
    
    if opcion == 1:
        print(f"La suma total es: ",suma)
    elif opcion == 2:
        print(f"El Número mayor es: {mayor}")
    elif opcion == 3:
        print(f"El Número menor es: {menor}")
    elif opcion == 4:
        print(f"El promedio obtenido es: {promedio:.2f}")
    elif opcion == 5:
        print("-" * 40)
        print("Distribución por unidades, decenas, centenas y millares:")
        print(f"Unidades: {numero_unidades}")
        print(f"Decenas: {numero_decenas}")
        print(f"Centenas: {numero_centenas}")
        print(f"Millares: {numero_millares}")
        print("-" * 40)
    elif opcion == 0:
        print("¡Hasta pronto!")
    else:
        print("Opción no válida.")

