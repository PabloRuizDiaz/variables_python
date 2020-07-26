#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pablo"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    print('Ingrese el primer número entero a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número entero a operar:')
    numero_2 = int(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    print('1er numero ingresado', numero_1, 'y 2do', numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
    suma_1 = numero_1 + numero_2
    print('La suma es', suma_1)

    # Resta
    resta_1 = numero_1 - numero_2
    print('La resta es', resta_1)

    # División
    division_1 = numero_1 / numero_2
    print('La division es',division_1)

    # Multiplicación
    multi_1 = numero_1 * numero_2
    print('La multiplicacion es',multi_1)


def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números reales
    print('Ingrese el primer número a operar:')
    numero_3 = float(input())

    print('Ingrese el segundo número a operar:')
    numero_4 = float(input())

    # Alumno: Imprima en pantalla los dos números reales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_3, numero_4
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    suma_2 = numero_3 + numero_4
    print('La suma es', suma_2)

    # Resta
    resta_2 = numero_3 - numero_4
    print('La resta es', resta_2)

    # División
    division_2 = numero_3 / numero_4
    print('La division es',division_2)

    # Multiplicación
    multi_2 = numero_3 * numero_4
    print('La multiplicacion es',multi_2)


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    print(nombre + ' ' + apellido, 'o', nombre, apellido)

    # Almacenar su nombre completo en una variable
    nombre_completo = nombre +' ' + apellido
    
    # Imprimir la cantidad de letras que posee su nombre completo
    print('La longitud de su nombre completo es', len(nombre_completo))


def ej3():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

    print(palabra_1.upper()[0] + palabra_2.upper()[0] + palabra_3.upper()[0])


def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    letra_1 = palabra_1[:3]
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    letra_2 = palabra_2[-3:]
    # Formar una nueva palabra con los recortes solicitados
    letra_3 = letra_1 + letra_2
    # Imprima en pantalla los resultados
    print(letra_3)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
