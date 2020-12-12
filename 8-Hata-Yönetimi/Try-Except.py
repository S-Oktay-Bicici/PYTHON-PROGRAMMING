
sayı1 = int(input("Birinci sayıyı giriniz :"))
sayı2 = int(input("İkinci sayıyı giriniz : "))

try:
	sonuç = sayı1/sayı2
	print("sonuç : ",sonuç)

except ZeroDivisionError:
	print("Sayı sıfıra bölünemez lütfen başka sayı giriniz : ")
	
##########################################################################

try:
	sayı1 = int(input("Birinci sayıyı giriniz :"))
	sayı2 = int(input("İkinci sayıyı giriniz  : "))
	sonuç = sayı1/sayı2
	print("sonuç : ",sonuç)

except ZeroDivisionError:
	print("Sayı sıfıra bölünemez lütfen başka sayı giriniz : ")

except ValueError:
	print("Karakter girmeyiniz. Lütfen sayı giriniz : ")

##########################################################################

try:
	sayı1 = int(input("Birinci sayıyı giriniz :"))
	sayı2 = int(input("İkinci sayıyı giriniz  : "))
	sonuç = sayı1/sayı2
	print("sonuç : ",sonuç)

except ZeroDivisionError:
	print("Sayı sıfıra bölünemez lütfen başka sayı giriniz : ")

except ValueError:
	print("Karakter girmeyiniz. Lütfen sayı giriniz : ")

except:
	print("Beklenmeyen bir hata oluştu. Lütfen sonra tekrar deneyniz.")
	
##########################################################################

try:
	sayı1 = int(input("Birinci sayıyı giriniz :"))
	sayı2 = int(input("İkinci sayıyı giriniz  : "))
	sonuç = sayı1/sayı2
	print("sonuç : ",sonuç)

except ZeroDivisionError as açıklama:
	print(açıklama)
	print("Sayı sıfıra bölünemez lütfen başka sayı giriniz : ")

###########################################################################

try:
	sayı1 = int(input("Birinci sayıyı giriniz :"))
	sayı2 = int(input("İkinci sayıyı giriniz  : "))
	sonuç = sayı1/sayı2
	print("sonuç : ",sonuç)

except ZeroDivisionError:
	print("Sayı sıfıra bölünemez lütfen başka sayı giriniz : ")

except ValueError:
	print("Karakter girmeyiniz. Lütfen sayı giriniz : ")

finally:
	print("Her durumda çalışıyorum.")

######################################################################

yarıçap = int(input("Yarıçapı giriniz : "))
pi = 3.14
if yarıçap<=0:
	raise ValueError("Yarıçap sıfır ve sıfırdan küçük bir değer olamaz. 
		                Lütfen farklı bir sayı giriniz.")

sonuç = pi*(yarıçap**2)
print("Alan : {}'dir.".format(sonuç))
