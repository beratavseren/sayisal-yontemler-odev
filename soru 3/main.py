def f(x):
    e=2.71828
    return 4*(e**(-0.5*x))-x

def turev(x):
    e = 2.71828
    return -(2+(e**(1/2*x)))/(e**(1/2*x))

x_ilk=2
kontrol=0
while(kontrol<4):
    gecici = x_ilk - (f(x_ilk)/turev(x_ilk))
    x_ilk=gecici
    kontrol=kontrol+1
    print(x_ilk)