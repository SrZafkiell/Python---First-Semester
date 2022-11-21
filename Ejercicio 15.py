#2.92897
# where a is the number to be print
# print("%.3f" % a)
# print("{:.3f}".format(a))
resultado = 0
for i in range(1,11,1):
    resultado = resultado + 1/i
    
print("{:.5f}".format(resultado))