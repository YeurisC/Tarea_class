'''
    Calculadoras hecha en python
'''
#aloja el nombre del usuario
nombre = input("¿Cual es tu nombre? ")

resp = 's'
while resp == 's':
    #TODO:
    #sumar, restar, multiplicar y dividir
    print("Bienvenido a tu calculadora personal", nombre)

    numero1 = int(input('Ingrese el valor 1: '))
    numero2 = int(input('ingrese valor 2: '))
    suma = numero1 + numero2
    resta = numero1 - numero2
    division = numero1 / numero2

    #suma
    print(f"la suma es:{suma}")
    print(f"la resta es:{resta}")
    print(f"la division es:{division}")
    #pregunta para proxima ejecución
    resp = input('Desea volver a ejecutar(S/N): ')