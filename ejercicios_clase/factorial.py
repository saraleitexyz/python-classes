
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n - 1)

def factorial2(n):
    acum = 1
    for i in range(2, n + 1):
        acum *= i
    return acum

#for i in range(0, 100):
#    print("Número:", i, "Factorial:", factorial2(i))
supernumero=factorial2(500)
longitud=len(str(supernumero))
print("Factorial:", supernumero, "Longitud", longitud)
