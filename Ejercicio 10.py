'''
Inicio
	pedirNombre: String
    pedirEdad : Entero
    pedirCantidadCamisetas: Entero
    
    si (pedirEdad < 18)
    	totalPagar = cantidadCamisetas * 30000
    	tipoCamiseta = "Juvenil"
        mostrar (nombre)
        mostrar (tipoCamiseta)
        mostrar (totalPagar)
    si (pedirEdad >= 18)
        totalPagar = cantidadCamisetas * 45000
    	tipoCamiseta = "Adulto"
        mostrar (nombre)
        mostrar (tipoCamiseta)
        mostrar (totalPagar)
FIN
'''

nombre = str(input())
edad = int(input())
cantidadCamisetas = int(input())

if (edad < 18):
    totalPagar = cantidadCamisetas * 30000
    tipoCamiseta = "Juvenil"
    print("NOMBRE:", nombre)
    print("TIPO CAMISETA:", tipoCamiseta)
    print("TOTAL A PAGAR:", totalPagar)
elif (edad >= 18):
    totalPagar = cantidadCamisetas * 45000
    tipoCamiseta = "Adulto"
    print("NOMBRE:",nombre)
    print("TIPO CAMISETA:", tipoCamiseta)
    print("TOTAL A PAGAR:", totalPagar)