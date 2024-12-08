def suma_cifrelor(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma
print(suma_cifrelor(1234))