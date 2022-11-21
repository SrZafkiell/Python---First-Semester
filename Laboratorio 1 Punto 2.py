# Author: Daniel Alejandro Ceron Rayo
# Software development student at Universidad del Valle Cali-Colombia / 1st semester
# Professor: Giovanny Hidalgo / FUNDAMENTOS DE PROGRAMACION IMPERATIVA
'''
Lab 1 - 2/2 
Spanish:
Desarrollar un programa que permita evaluar una función por partes. Dado un valor de x se calcula el valor de f(x) utilizando la funcion que se muestra a continuación:


https://raw.githubusercontent.com/jose-llanos/Prueba/main/EcuacionPartes.png

El programa a desarrollar debe definir una función en la que se calcula el valor de f(x). Probar el programa para los tres valores de x que se muestran en las entradas a continuación:

NOTA 1: Recuerde que en las entradas no debe llevar texto Ejemplo: la entrada peso se escribe: peso = float(input()) en cambio en las salidas, si debe llevar texto. Ejemplo: print ("Categoria: Infrapeso") o print ("PACIENTE:",nombre_variable)

NOTA 2: Recuerde que si el ejercicio no tiene documentación o es incorrecta, es un punto no valido
English: 
'''

"""
PSEUDOCÓDIGO

INICIO

    PEDIR xValue : Integer

    SI (xValue <= 0)
        IMPRIMIR ("f(x)=",(8*xValue**2)-6)
    SINO SI (xValue > 0)
        IMPRIMIR ("f(x)=",(3*xValue)+5)

FIN

NOTAS
f(x) si x menor o igual a 0 -> 8x^2 - 6
f(x) si x mayor a 0 -> 3x+5

"""

xValue = int(input())
if xValue <= 0:
    print("f(x)=",(8*xValue**2)-6)
elif xValue > 0:
    print("f(x)=",(3*xValue)+5)