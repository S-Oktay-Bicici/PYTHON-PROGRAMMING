# aşşağıdaki tekrarlama dizisi pozitif tam sayılar için tasarlanmıştır

#n -> n\2 ( n çift)
#n -> 3n+1 (n tek)

# 13 den başlayarak diziyi üretiniz 

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# 1 milyon altındaki hangi başlangıç sayısı en uzun zinciri üretir

enuzun = 0
aranan = 0
for sayi in range(999999, 300000,-1):
    zincir = 0
    n = sayi
    while n! = 1:
        zincir += 1
        if n%2 == 0:
            n //= 2
        else: 
            n = 3*n+1
    if zincir>enuzun:
        enuzun = zincir
        aranan = sayi

print("Zincir sayısı: ",enuzun,"Sayımız: ",aranan)