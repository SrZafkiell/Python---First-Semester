# Desarrollar una función que permita calcular el valor de f(a,b) definida de la siguiente manera:
# f(a,b) = 3a^2+2ab-7

# def funcionPrueba(a, b):
#     print("f(a,b) =",(3*a**2)+((2*a*b)-7))

# a = int(input())
# b = int(input())

# funcionPrueba(a,b)

def funcionPrueba(a, b):
    return ((3*a**2)+((2*a*b)-7))

a = int(input())
b = int(input())

print("f(a,b) =",funcionPrueba(a,b))

