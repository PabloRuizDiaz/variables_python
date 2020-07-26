#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "PabloRuizDiaz"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice una calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia

    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''
  
    print('Se realizara la suma de dos numeros, favor de ingresarlos separados por la tecla ENTER (numeros decimales con ".")')
    numero_1 = float(input())
    numero_2 = float(input())

    suma = numero_1 + numero_2
    print('La suma de', numero_1, 'y',numero_2, 'es', suma)


def ej2():
    print('\n')
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona

    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''

    print('Favor de ingresar su nombre completo, y finalizar con ENTER:')
    nombre = str(input())
    print('Favor de ingresar su DNI completo (sin puntos), y finalizar con ENTER:')
    dni = int(input())
    print('Favor de ingresar su edad, y finalizar con ENTER:')
    edad = int(input())
    print('Favor de ingresar su altura (unidad en cm), y finalizar con ENTER:')
    altura = float(input())

    print('El Nombre completo ingresado es', nombre, 'y su DNI es', dni)
    print(nombre, 'tiene una edad de',edad,'y una altura de', altura, 'cm')


def ej3():
    print('\n')
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''

    print('Favor de ingresar el 1er nombre completo del Padre o Madre (Nombre, Apellido), y finalizar con ENTER:')
    nombre_1 = str(input())
    print('Favor de ingresar el 2do nombre completo del Padre o Madre (Nombre, Apellido), y finalizar con ENTER:')
    nombre_2 = str(input())
    print('Favor de ingresar el nombre del hijo/a, y finalizar con ENTER:')
    nombre_3 = str(input())

    print('La nueva persona ingresada tiene la posibilidad de tener su nombre completo como:')
    print(nombre_3, nombre_1.split(', ')[1], nombre_2.split(', ')[1])
    print(nombre_3, nombre_2.split(', ')[1], nombre_1.split(', ')[1])


def ej4():
    # Ejercicios de práctica con cadenas
    print('\n')
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''

    print('Ingresar Nombre y Apellido (Nombre, Apellido) de la 1ra persona, y finalizar con ENTER:')
    persona_1 = str(input())
    print('Ingresar Nombre y Apellido (Nombre, Apellido) de la 2da persona, y finalizar con ENTER:')
    persona_2 = str(input())

    print('Tienen parentezco la 1ra Persona con la 2da?', persona_2.split(', ')[1] in persona_1)


def ej5():
    # Ejercicios de práctica con cadenas
    print('\n')
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''

    print('Introduzca su nombre completo por favor:')
    nombre = str(input())

    print('\n')
    print(nombre.lower())
    print(nombre.upper())
    print(nombre.capitalize())


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
