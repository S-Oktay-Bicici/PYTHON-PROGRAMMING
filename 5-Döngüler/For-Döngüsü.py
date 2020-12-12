#########################################################
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

sayi = 0

for harf in alfabe:
	print(harf,end = "")
	sayi += 1

print(sayi)

##########################################################
 
for sayi in range(0,100):
	print(sayi)

#0 dan başlayacaksa yazmaya gerek yok 
for sayi in range(100):
	print(sayi)

#2 şer olarak artmasını istiyoruz
for sayi in range(0,100,2):
	print(sayi)
	
#############################################################

for k in range(-1000,1000):
	for v in range(-1000,1000):
		if k is v:
			print(k)

############################################################

sayılar = "123456789"

for i in sayılar:
	if int(i) > 3:
		print(i)

#############################################################

print(*range(10))

print(*range(10), sep=", ")

############################################################

liste = [5,4,3,2,1]
for sayı in liste:
	print("sayı : ",sayı)

############################################################

liste = [10,9,8,7,6,5,4,3,2,1]
for sayı in liste:
	if(sayı%2!=0):
		print("sayı : ",sayı)

################################################################

sayılar = (10,9,8,7,6,5,4,3,2,1)
for sayı in sayılar:
	print("sayılar : ",sayı)

#################################################################

topla = [(10,9,8),(7,6,5),(4,3,2),(1,0,-1)]
for a,b,c in topla:
	print("toplamları : ",a+b+c)

################################################################

günler = ("1.gün":"pazartesi","2.gün":"salı","3.gün":"çarşamba")
for değişken in günler:
	print(değişken)

#################################################################3
