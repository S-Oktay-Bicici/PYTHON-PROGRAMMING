
vize = int(input("Vize notu : "))
final = int(input("Final notu : "))
ortalama = (vize*0.4)+(final*0.6)

if (ortalama >= 85):
	print("Harf notunuz : AA")
elif (ortalama >= 70 and ortalama <85):
	print("Harf notunuz : BA")
elif (ortalama >= 60 and ortalama <70):
	print("Harf notunuz : BB")
elif (ortalama >= 45 and ortalama <60):
	print("Harf notunuz : CB")
elif (ortalama >= 40 and ortalama <45):
	print("Harf notunuz : CC")
elif (ortalama >= 35 and ortalama <40):
	print("Harf notunuz : DC")
elif (ortalama >= 30 and ortalama <35):
	print("Harf notunuz : DD")
else:
	print("Derten kaldınız.")

########################################################
x = int(input("x değerini giriniz :"))

if x == 5:
	print("Girdiğiniz değer :",x)
else:
	print("Girdiğiniz değer",x,"değil.")
	
y = input("y değerini giriniz :")

if bool(y):
	print("içerisi dolu")
else:
	print("içerisi boş")

####################2###################################
sayı = int(input("Bir sayı giriniz: "))

if sayı > 10: 
	print("Girdiğiniz sayı 10'dan büyüktür!")
elif sayı < 10: 
	print("Girdiğiniz sayı 10'dan küçüktür!")
elif sayı == 10: 
	print("Girdiğiniz sayı 10'dur!")

######################3##################################

yaş = int(input("Yaşınız: "))

if yaş == 18: 
	print("18 iyidir!")
elif yaş < 0: 
	print("Yok canım, daha neler!...")
elif yaş < 18: 
	print("Genç bir kardeşimizsin!")
elif yaş > 18: 
	print("Eh, artık yaş yavaş yavaş kemale eriyor!")

######################yada bu şekilde yazabiliriz############

yaş = int(input("Yaşınız: "))

if yaş == 18: 
	print("18 iyidir!")
if yaş < 0: 
	print("Yok canım, daha neler!...")
if yaş < 18:
	print("Genç bir kardeşimizsin!")
if yaş > 18: 
	print("Eh, artık yaş yavaş yavaş kemale eriyor!")

########################4########################################

boy = int(input("boyunuz kaç cm?"))

if boy < 170: 
	print("boyunuz kısa")
elif boy < 180: 
	print("boyunuz normal")
else: 
	print("boyunuz uzun")

##################################################################

kullanıcı_adı = input("Kullanıcı adınız: ")
parola        = input("Parolanız : ")

toplam_uzunluk = len(kullanıcı_adı) + len(parola)

mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"

print(mesaj.format(toplam_uzunluk))

if toplam_uzunluk > 40: 
	print("Kullanıcı adınız ile parolanızın ","toplam uzunluğu 40 karakteri geçmemeli!")
else: 
	print("Sisteme hoşgeldiniz!")


#####################################################################


