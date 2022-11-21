"""
Desarrollar dos funciones, una que calcula el el área de un círculo y otra para el perímetro de un círculo.
Usar las funciones tres veces para calcular el área y el perímetro de los círculos con los siguientes tres radios:

radio: 1.5
Área del círculo: 7.069
Perímetro del círculo: 9.4248

radio: 5.4
Área del círculo: 91.609
Perímetro del círculo: 33.9292
"""
import math

def areaCirculo(radio):
    return math.pi*(radio**2)

def perimetroCirculo(radio):
    return radio*2*math.pi

for i in range(0,3,1):
    radio = float(input())
    print("Área del círculo:","{:.3f}".format(areaCirculo(radio)))
    print("Perímetro del círculo:","{:.4f}".format(perimetroCirculo(radio)))

#"{:.5f}".format( args )
# where a is the number to be print
# print("%.3f" % a)
# print("{:.3f}".format(a))