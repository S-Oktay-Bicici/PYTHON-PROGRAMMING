#öncelikle dosya işlemleri için os kütüphanesini ekliyoruz
import os

#dosyanın ismini öğrenebiliriz
with open("deneme.txt") as dosya:
	print(("Dosya ismi : ",dosya.name))

#dosyanı hangi modda olduğunu öğreniriz
with open("deneme.txt") as dosya:
	print("Dosya modu : ",dosya.mode)


#dosyanın kapalı olup olmamasını kontrol eder 
with open("deneme.txt") as dosya:
	print("Dosya kapalı mı : ",dosya.closed)


#dosyanın yazma modunda olup olmamasını kontrol eder 
with open("deneme.txt") as dosya:
	print("Dosyaya yazılabilir mi : ",dosya.writable())


#dosyanın okuma modunda olup olmamasını kontrol eder 
with open("deneme.txt") as dosya:
	print("Dosya okunabilir mi : ",dosya.readable())

