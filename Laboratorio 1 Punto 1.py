# Author: Daniel Alejandro Ceron Rayo
# Software development student at Universidad del Valle Cali-Colombia / 1st semester
# Professor: Giovanny Hidalgo / FUNDAMENTOS DE PROGRAMACION IMPERATIVA

'''
Lab 1 - 1/2 
Spanish: 
Enunciado del problema
Al ingresar a un centro médico se solicitan los siguientes datos para cada paciente: nombre, peso (kg) y altura (mts). Se debe calcular el índice de masa corporal (IMC=peso/(altura)^2) e identificar la categoría que tiene el paciente según el valor calculado. Hay tres categorías que se pueden identificar según el IMC, éstas son: Infrapeso, Normal y Sobrepeso. Las categorías se calculan utilizando la siguiente tabla:

IMC	Categoría
IMC < 18.5	Infrapeso
18.5 >= IMC < 25.0	Normal
IMC >= 25.0	Sobrepeso

Desarrollar un programa que defina una función donde se calculen los valores de salida para un paciente. Utilizar la función para los tres pacientes que se muestran en los casos de pruebas

NOTA 1: Recuerde que en las entradas no debe llevar texto Ejemplo: la entrada peso se escribe: peso = float(input()) en cambio en las salidas, si debe llevar texto. Ejemplo: print ("Categoria: Infrapeso") o print ("PACIENTE:",nombre_variable)

NOTA 2: Recuerde que para agregar o quitar valores despues del . flotante se puede utilizar: format(nombre_variable,".4f")) donde el número 4 es la cantidad de valores a agregar.

NOTA 3: Recuerde que si el ejercicio no tiene documentación o es incorrecta, es un punto no valido
English: 
'''

"""
PSEUDOCÓDIGO

INICIO

    PEDIR nombre : String
    PEDIR peso, altura : Float

    imc = weight/(height**2)

    SI (imc < 18.5)
        category = "Infrapeso"
    SINO SI (18.5 >= imc < 25.0)
        category = "Normal"
    SINO SI (imc >= 25.0)
        category = "Sobrepeso"

    IMPRIMIR (PACIENTE: nombre)
    IMPRIMIR (IMC: imc)
    IMPRIMIR (Categoria: category)

FIN

NOTAS

(IMC=peso/(altura)^2)

IMC	Categoría
IMC < 18.5	Infrapeso
18.5 >= IMC < 25.0	Normal
IMC >= 25.0	Sobrepeso

"%.3f" % data
"""

name = str(input())
weight = float(input())
height = float(input())
category = ""

imc = weight/(height**2)

if imc < 18.5:
    category = "Infrapeso"
elif imc >= 18.5 and imc < 25.0:
    category = "Normal"
elif imc >= 25.0:
    category = "Sobrepeso"

if category != "":
    print("PACIENTE:", name)
    print("IMC:", "%.4f" % imc)
    print("Categoria:", category)
