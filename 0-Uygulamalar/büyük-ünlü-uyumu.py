def buyukuyum(kelime):
    kalin = ['a','ı','o','u']
    ince = ['e','i','ö','ü']
    k_sayisi = 0
    i_sayisi = 0
    for harf in kelime:
        if harf in kalin:
            k_sayisi += 1
        elif harf in ince:
            i_sayisi += 1
    if k_sayisi == 0 or i_sayisi == 0:
        return True
    else:
        return False

for giris in range(5):
    kelime = input("Bir kelime giriniz: ")
    if buyukuyum(kelime):
        print(kelime, "büyük ünlü uyumuna uyuyor.")
    else:
        print(kelime, "büyük ünlü uyumuna uymuyor.")