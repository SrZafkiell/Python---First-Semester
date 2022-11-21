years = int(input())

if years > 0:
    shirtQuantity = int(input())
    if years >= 5 and years <= 10:
        shirtType = str("Mini")
        totalPrice = 15000 * shirtQuantity

    elif years > 10 and years < 16:
        shirtType = str("Juvenil")
        totalPrice = 20000 * shirtQuantity

    elif years >= 16 and years <= 18:
        shirtType = str("Adolescente")
        totalPrice = 30000 * shirtQuantity

    elif years > 18:
        if years >= 60 and years <= 80:
            shirtType = str("Premium")
            totalPrice = 12000 * shirtQuantity
        else: 
            shirtType = str("Adulto")
            totalPrice = 50000 * shirtQuantity
    

    print("TIPO CAMISETA:",shirtType)
    print("TOTAL A PAGAR:",totalPrice)
