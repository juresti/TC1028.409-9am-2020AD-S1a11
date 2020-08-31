def sumaFibonacci():
    ult = 1
    pen = 0
    res = ult + pen
    bueno = res
    while (res < 1000):
        pen = ult
        ult = res
        res = ult + pen
        bueno = ult
        #print(res)
    
    return bueno