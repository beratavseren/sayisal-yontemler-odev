import math as mat


def maclaurin(n, x):
    a = mat.pow(-1, n)
    b = mat.pow(x, 2*n)
    c = (mat.factorial(2*n))
    sonuc = (a*b)/c
    if n >= 0:
        return sonuc
    else:
        print("n sıfırdan büyük olmalıdır")


pi = 3.14
ilkTerim = maclaurin(0, pi/5)
ikinciTerim = maclaurin(1, pi/5)
sonuc = ikinciTerim+ilkTerim
sapmaPayi = mat.cos(pi/5)-sonuc


print("maclaurin ilk terim sonucu:")
print(ilkTerim)

print("maclaurin ilk terim sapma payı:")
print(mat.cos(pi/5)-ilkTerim)

print("maclaurin ilk 2 terim sonucu:")
print(sonuc)

print("ilk 2 terim sapma payi:")
print(sapmaPayi)

print("gerçek değer:")
print(mat.cos(pi/5))
