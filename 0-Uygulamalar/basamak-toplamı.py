#klavyeden girilecek x ve y sayılarından oluşacak x**y sayısının
#basamakları toplamını hesaplayan fonksiyonu yazınız

def basamaktoplam(x,y):
    sayi = x**y 
    toplam = 0

    for rakam in str(sayi):
        toplam += int(rakam)
    return toplam

taban = int(input("Tabanı giriniz: "))
us = int(input(Üssü giriniz: "))

print(basamaktoplam(taban,us))

