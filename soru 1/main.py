def denklem(x):
    sonuc=x*x*x-2*x*x-5
    return sonuc


x_alt=2
x_ust=4
x_kok=(x_alt+x_ust)/2
kontrol=0
print(x_kok)
while (kontrol<3):
    if(denklem(x_alt)*denklem(x_kok)<0):
        x_ust=x_kok
        x_kok=(x_ust+x_alt)/2
    elif(denklem(x_ust)*denklem(x_kok)<0):
        x_alt=x_kok
        x_kok=(x_alt+x_ust)/2
    kontrol=kontrol+1
    print(x_kok)
