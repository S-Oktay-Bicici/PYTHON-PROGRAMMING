from random import randint

sayi = randint(1,50)
bilindi = False
hak = 5

for n in range(hak):
    tahmin = int(input("Sayıyı tahmin ediniz: "))
    if sayi == tahmin:
        print("Tebrikler bildiniz.")
        bilindi = True
        break
    elif tahmin > sayi and n != hak-1:
        print("Aşağı in!")
    elif tahmin < sayi and n != hak-1:
        print("Yukarı çık!")

if not bilindi:
    print("Sayi",sayi,"idi.")