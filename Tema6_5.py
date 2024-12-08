def putere(a, b):
    if b == 0:
        return 1
    return a * putere(a, b -1)

print(putere(2,3))
