def denklem(x):
    sonuc=x*x*x+4*x*x-10
    return sonuc
def mutlakDegerCikar(a,b):
    sonuc=a-b
    if(sonuc<0):
        sonuc=sonuc*(-1)
    return sonuc
def mutlakDeger(c):
    if(c<0):
        c=c*(-1)
    return c


x_alt=1
x_ust=2
x_kok=(x_alt+x_ust)/2
kontrol=0
bagilHata=1
print("bagilHatayı whileda bagilHata<0.000001 yazınca döngüye girmiyor bu şekilde kontrolle yapınca da sayı küçülünce 8.942144326209425e-05 gibi sayılara gidiyor")
print(x_kok)
while (kontrol<15):
    if(denklem(x_alt)*denklem(x_kok)<0):
        x_ust=x_kok
        x_kok=(x_ust+x_alt)/2
        bagilHata = mutlakDegerCikar(x_kok, x_ust) / mutlakDeger(x_kok)
    elif(denklem(x_ust)*denklem(x_kok)<0):
        x_alt=x_kok
        x_kok=(x_alt+x_ust)/2
        bagilHata=mutlakDegerCikar(x_kok,x_alt)/mutlakDeger(x_kok)
    kontrol=kontrol+1
    print(x_kok)
    print(bagilHata)