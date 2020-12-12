from os import system as komut

class Musteri():
    def __init__(self, ID, PAROLA, ISIM):
        self.isim = ISIM
        self.id = ID
        self.parola = PAROLA
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self, ID:str, PAROLA:str, ISIM:str):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))
        print("BAnkamıza kayıt yaptığınız için teşekkürler!")
        input("Ana menüye dönmek için 'enter'e basın!")

def main():
    banka = Banka()
    while True:
        komut("clear")
        print("""
        [1] Banka Müşterisiyim
        [2] Banka Müşterisi Olmak İstiyorum
        """)

        secim = input("Seçiniz: ")

        if secim == "1":
            ids = [i.id for i in banka.musteriler]
            ID = input("ID: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID == musteri.id:
                        print("Hoşgeldiniz {} ".format(musteri.isim))
                        parola = input("Parolanız: ")
                        if parola == musteri.parola:
                            print("Giriş Başarılı.")
                            while True:
                                komut("clear")
                                print("""
                                [1] Bakiye Sorgulama
                                [2] Para Yatır (Kendi Hesabına)
                                [3] Para Yatır (Başkasının Hesabına)
                                [4] Para Çek 
                                [Q] Çıkış
                                """)

                                secim2 = input("İşlemini: ")

                                if secim2 == "1":
                                    print("Bakiyeni {} ".format(musteri.bakiye))
                                    input("Ana menüye dönmek için 'enter'e basın!")

                                elif secim2 == "2":
                                    miktar = int(input("Miktar: "))
                                    onay = input("Kendi hesabınıza {} TL para yatırma işlemini onaylıyor musunuz ?: E/H\n".format(miktar))
                                    if onay == "E" or onay == "e":
                                        musteri.bakiye += miktar
                                        print("Paranız yatrırıldı!")
                                        input("Ana menüye dönmek için 'enter'e basın!")

                                    elif onay == "H" or onay == "h":
                                        print("İşlem iptal edildi!")
                                        input("Ana menüye dönmek için 'enter'e basın!")

                                    else:
                                        print("Hatalı girildi işlem iptal!")

                                elif secim2 == "3":
                                    arananID = input("Müşteri ID: ")
                                    if arananID in ids:
                                        for digerMusteri in banka.musteriler:
                                            if arananID  == digerMusteri.id:
                                                miktar = int(input("Miktar: "))
                                                if miktar <= musteri.bakiye:
                                                    onay = input("{} adlı nüşterimize  {} TL para yatırma işlemini onaylıyor musunuz ?: E/H\n".format(digerMusteri.isim,miktar))
                                                    if onay == "E" or onay == "e":
                                                        digerMusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar
                                                        print("Paranız yatrırıldı!")
                                                        input("Ana menüye dönmek için 'enter'e basın!")

                                                    elif onay == "H" or onay == "h":
                                                        print("İşlem iptal edildi!")
                                                        input("Ana menüye dönmek için 'enter'e basın!")

                                                    else:
                                                        print("Hatalı girildi işlem iptal!")
                                                        input("Ana menüye dönmek için 'enter'e basın!")
                                                else:
                                                    print("Bakiyeniz bu işlem için yetersiz!")
                                                    input("Ana menüye dönmek için 'enter'e basın!")

                                    else:
                                                print("Müşteri bulunumadı!")
                                                input("Ana menüye dönmek için 'enter'e basın!")
                                
                                elif secim2 == "4":
                                    miktar = int(input("Mİktar: "))
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        print("İşlem tamamlandı, paranızı alınız!")
                                        input("Ana menüye dönmek için 'enter'e basın!")
                                    else:
                                        print("Bakiyeniz bu işlem için yeterli değildir!")
                                        input("Ana menüye dönmek için 'enter'e basın!")

                                elif secim2 == "Q"or secim2 == "q":
                                    break
        elif secim == "2":
            ID = input("ID: ")
            ISIM = input("İsminiz: ")
            PAROLA = input("Parola: ")
            banka.musteri_ol(ID,PAROLA,ISIM)


if __name__ == "__main__":
    main()