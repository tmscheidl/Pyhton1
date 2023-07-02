def round_(number, ndigits: int = None):
    if ndigits is None:
        result = (int(number + 0.5))
        return print("round_("+str(number)+") =", int(result))
    else:
        result = (int(pow(10,ndigits)*number + 0.5)) / pow(10,ndigits)
        return print("round_("+str(number)+", "+str(ndigits)+") =", result)
    
round_(777.777)
round_(777.777, 0)
round_(777.777, 1)
round_(777.777, 2)
round_(777.777, 3)
round_(777.777, 4)
round_(777.777, -1)
round_(777.777, -2)
round_(777.777, -3)
round_(777.777, -4)
