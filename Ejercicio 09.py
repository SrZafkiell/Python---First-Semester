articleOnePrice = 30000 # Libro electronico
articleTwoPrice = 45000 # Libro empreso
articleThreePrice = 8000 # Revista

shopIvaPercentage = 19

articleType = int(input())
articleQuantity = int(input())

if articleType == 1 or 2 or 3:
    if articleType == 1:
        ivaPrice = (articleOnePrice * shopIvaPercentage)/100
        totalPrice = articleOnePrice * articleQuantity
    elif articleType == 2:
        ivaPrice = (articleTwoPrice * shopIvaPercentage)/100
        totalPrice = articleTwoPrice * articleQuantity
    elif articleType == 3:
        ivaPrice = (articleThreePrice * shopIvaPercentage)/100
        totalPrice = articleThreePrice * articleQuantity
        
    print("Precio de venta:",totalPrice)
    print("IVA:",int(ivaPrice))