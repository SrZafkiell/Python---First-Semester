import math

# where a is the number to be print
# print("%.3f" % a)
# print("{:.3f}".format(a))

figureType = int(input())

if figureType == 1 or 2:
    if figureType == 1:
        cubeSide = int(input())
        print("El área del cuadrado es:",cubeSide**2)
    elif figureType == 2:
        circleRadius = float(input())
        print("El área del círculo es:", "%.3f" % (math.pi*circleRadius**2))