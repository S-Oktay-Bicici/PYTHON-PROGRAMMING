import os

masalar = dict()
for i in range(10):
    masalar[i] = 0


def hesapEkle():
    masaNo = int(input("Masa No: "))
    gecerli = masalar[masaNo]
    eklenecek = float(input("Eklenecek Ücret: "))
    toplam = gecerli + eklenecek
    masalar[masaNo] = toplam


def hesapSil():
    masaNo = int(input("Masa No: "))
    gecerli = masalar[masaNo]
    eksilecek = float(input("Çıkarılacak Ücret: "))
    toplam = gecerli - eksilecek
    if toplam < 0:
        print("İşlemde hata var, kontrol ediniz!")
    else:
        masalar[masaNo] = toplam



def  hesapKontrol(dosya_adi):
    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag = True

    except FileNotFoundError:
        dosya = open(dosya_adi,"w")
        dosya.close()
        print("İlk kez çalıştırıldı! Kayıt dosyası oluşturuldu!")
        flag = False

    if flag:
        for i in enumerate(veriler):
            masalar[i[0]] = float(i[1])

    else:
        pass


def kayitGuncelle():
    dosya = open("kayıtlar.txt","w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret + "\n")

    dosya.close()


def main():
    hesapKontrol("kayıtlar.txt")
    while True:
        os.system("cls")
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [4] Çıkış 
        """)

        secim = input("İşleminiz: ")

        if secim == "1":
            for i in range(10):
                print("Masa {} için hesap: {}".format(i,masalar[i]))
            print("İşlem tamamlandı! Ana menüye dönmek için 'enter'e bas!")
            input()

        elif secim == "2":
            hesapEkle()
            print("İşlem tamamlandı! Ana menüye dönmek için 'enter'e bas!")
            input()

        elif secim == "3":
            hesapSil()
            print("İşlem tamamlandı! Ana menüye dönmek için 'enter'e bas!")
            input()

        elif secim == "q" or secim == "Q":
            print("Çıkılıyor!")
            quit()


main()
