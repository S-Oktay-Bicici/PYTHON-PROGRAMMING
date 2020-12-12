
a = 0
while(a<10):
	print("merhaba")
	a+=1

a = 0
while(a<10):
	print("merhaba")
	break
	a+=1

######################################################################

liste = [5,4,3,2,1]
for sayı in liste:
	print("sayı :",sayı)


liste = [5,4,3,2,1]
for sayı in liste:
	print("sayı :",sayı)
	break

liste = [5,4,3,2,1]
for sayı in liste:
	break
	print("sayı :",sayı)

##########################################################################

liste = [5,4,3,2,1]
for sayı in liste:
	continue
	print("sayı :",sayı)

########################################################################

for sayı in range(10):
	if(saı%2==0):
		continue
	else:
		print(sayı)

#########################################################################

a = 0
while(a<10):
	continue
	print("merhaba")
	a+=1

###########################################################################

while True:
	parola = input("parola belirleyin: ")
	
	if not parola:
		print("parola bölümü boş geçilemez!")
		
	elif len(parola) in range(3, 8): #eğer parolanın uzunluğu 3 ile 8 karakter #aralığında ise...
		print("Yeni parolanız", parola)
		break
	else:
		print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

#############################################################################

while True:
	sayı = int(input("Bir sayı girin: "))
	if sayı == 0:
		break
	
	elif sayı < 0:
		pass
	
	else:
		print(sayı)

#############################################################################

while True:
	parola = input("Lütfen bir parola belirleyiniz:")
	if len(parola) < 5:
		print("Parola 5 karakterden az olmamalı!")

	else:
		print("Parolanız belirlendi!")
		break

#############################################################################

while True:
	s = input("Bir sayı girin: ")
	
	if s == "iptal":
		break
	
	if len(s) <= 3:
		continue

	print("En fazla üç haneli bir sayı girebilirsiniz.")

############################################################################

