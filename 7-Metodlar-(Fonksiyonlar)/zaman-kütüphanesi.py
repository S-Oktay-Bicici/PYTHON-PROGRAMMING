from time import clock
print("Adınızı Giriniz: ", end="")
baslangicZamani = clock()
ad = input()
zaman = clock() - baslangicZamani
print(ad, "bilgilerinizi", zaman, "zamanda girdiniz")

"""

toplam = 0 # Toplam değişkeni tanımlanıp ilk değer olarak 0 veriliyor
basla = clock() # İşlem süresinin hesaplanması için süre başlatılıyor
for n in range(1, 1000001): # Toplamı alınacak sayılar için 1.000.000’e kadar döngü kuruluyor
 toplam += n #toplam = toplam + n
gecenZaman = clock() - basla # Geçen zaman hesaplanıyor
print("Toplam:", toplam, "Geçen Süre:", gecenZaman) # Sonuçlar  yazdırılıyor

"""
"""
sonDeger = 10000
sayac = 0
zaman = clock() # Süre başlatılıyor
# En küçük asal sayı olan 2 den istenilen değere kadar döngü kuruluyor
for deger in range(2, sonDeger + 1): # Sırayla sayılar ele alınıyor
    kontrol = True  # Değerlerin kontrol edilmesi için ilk değer True veriliyor
# Asal olma özelliğinin kontrolü için bölenlerinin döngüsü kuruluyor
    for bolenSayi in range(2, deger):
        if deger % bolenSayi == 0:
            kontrol = False  # Tam bölme işlemi oluştuysa kontrol False yapılıyor
            break  # ve döngü sonlandırılıyor
    if kontrol:
        sayac += 1  # Asal olma özelliği sağlanmışsa sayac arttırılıyor
print()  # Yeni satır başı
gecenZaman = clock() - zaman  # İşlem tamamlandıktan sonra süre sonlandırılıyor
print("Adet:", sayac, " Geçen Zaman:", gecenZaman, " saniye")

"""

"""

from time import sleep, clock
baslangic = clock()
for sayac in range(10, -1, -1): # Range 10, 9, 8, ..., 0
    print(sayac) # Sayac yazdırılıyor
    sleep(1) # 1 saniye bekleme işlemi yapılıyor
print(clock()-baslangic)

"""