çap = 16
yarıçap = çap / 2
pi = 3.14159

alan = pi * (yarıçap * yarıçap)
print(alan)

#sayının kuvvetini kısa yoldan hesaplam yolu
karesi = 12 ** 2
print(karesi)

#kuvvet hesaplamanın başka förmülü
karesi_2 = pow(12,2)
print(karesi_2)

#sayını belirtilen kuvveti alır 
#sonucu belirtilen sayıya bölüm kalanı değeri atar
sonuc = pow(11,3,4)
print(sonuc)

#sayının karakökünü hesaplıyoruz 
karekök = 144 ** 0.5
print(karekök)

######################################################################

print("T","B","M","M")

#sep parametresi ile virgülün çıktıda oluşturduğu boşluk yerine
#boşluk yerine gelicek değeri belirler 
print("T","B","M","M",sep = ".")

print("T","B","M","M",sep = ".",end = "\n")
print("Türkiye","Büyük","Millet","Meclisi")


print("T","B","M","M",sep = ".",end = "")
print("Türkiye","Büyük","Millet","Meclisi")

print("T","B","M","M",sep = ".",end = "------")
print("Türkiye","Büyük","Millet","Meclisi")

######################################################################

#float değeri yuvarlama işlemi yapıyoruz
a = round(2.55)
print(a)

#yuvarlama hassasiyetini belirliyoruz
b = round(2.55,1)
print(b)

#######################################################################
