#####################################################################
print("{} ve {} iyi bir ikilidir".format("Python", "Django"))

print("{} {}'ni seviyor!".format("Oktay", "Kendini"))

print("{} {} yaşında bir {}dur".format("Ahmet", "18", "futbolcu"))

#####################################################################

ad = input("Adınız nedir : ")
soyad = input("Soyadınız nedir : ")

print("Merhaba, adınız {} ve Soyadınız {}. ",format(ad,soyad))

#####################################################################

degisken1 = "oktay"
degisken2 = "biçici"

ifade1 = "{} {}".format(degisken1,degisken2)
ifade2 = "{} {}".format(degisken2,degisken1)

print(ifade1)
print(ifade2)

#####################################################################

degisken1 = "oktay"
degisken2 = "biçici"

ifade = "{AD} {SOYAD}".format(SOYAD = degisken2,AD = degisken1)

print(ifade)

#####################################################################

degisken1 = "oktay"
degisken2 = "biçici"

ifade = "|{:>15}|".format(degisken1)
ifade1 = "|{:<15}|".format(degisken2)
ifade2 = "|{:^15}|".format(degisken1)

print(ifade)
print(ifade1)
print(ifade2)

#####################################################################

#sadece string ifade girilebilir
ifade1 = "|{:s}|".format("oktay")

#sadece intiger ifade girilebilir
ifade2 = "|{:d}|".format(2020)

print(ifade1)
print(ifade2)

#####################################################################

#basamaklara ayırma
string = "{:,}".format(2136238213621)

print(string)

#####################################################################

#ASCII tablosundaki karşılığı
string = "--->>  {:c}".format

print(string)

#####################################################################

##########################################
#                                        #
#          DİLEKÇE TASLAĞI DENEMESİ      #
#                                        #
##########################################

dilekçe = """
                                               tarih: {}
                                               
			 T.C. {} ÜNİVERSİTESİ  
                   {} Fakültesi Dekanlığına
            
            
Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede
belirtilen mazeretim gereğince {} Eğitim-Öğretim Yılı {}.
yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.
Bilgilerinizi ve gereğini arz ederim.

                                                İmza
         
		Ad: {}
		Soyad : {}
		T.C. Kimlik No. : {}
		Adres : {}
		Tel.: {}
		Ekler : {}
"""

tarih           = input("tarih: ")
üniversite      = input("üniversite adı: ")
fakülte         = input("fakülte adı: ")
bölüm           = input("bölüm adı: ")
öğrenci_no      = input("öğrenci no. :")
öğretim_yılı    = input("öğretim yılı: ")
yarıyıl         = input("yarıyıl: ")
ad              = input("öğrencinin adı: ")
soyad           = input("öğrencinin soyadı: ")
tc_kimlik_no    = input("TC Kimlik no. :")
adres           = input("adres: ")
tel             = input("telefon: ")
ekler           = input("ekler: ")

print(dilekçe.format(tarih, üniversite, fakülte, bölüm,
							öğrenci_no, öğretim_yılı, yarıyıl,ad, soyad, tc_kimlik_no,adres, tel, ekler))

######################################################################

