#öncelikle dosya işlemleri için os kütüphanesini ekliyoruz
import os

print(os.getcwd())
#dosya uzantısını öğreniriz

"""
Dosya Açmak open(dosya_ismi,dosya_modu)

'r'  --->> Okuma(read)--> (dosya yoksa hata verir)

'w'  --->> Yazma(write)--> (dosya yoksa açar, hata vermez)(içindekini siler ve yazar)
'a'  --->> eklemek(appand)--> (dosya yoksa açar, hata vermez)
'x'  --->> oluşturmak(create)--> ( dosya varsa hata verir)

'r+' --->> Okuma ve Yazma (var olması gerekir)
'w+' --->> Okuma ve Yazma (varsa siler)
'a+' --->> Okuma ve Yazma 
'x+' --->> Okuma ve Yazma

dosya kapatmak için dosya.close()
"""

open("deneme.txt","w")

open("deneme2.txt","w")
dosya.close()


with open("deneme3.txt","w") as dosya:
	dosya.write("Python dersleri\n""oktay biçici")

with open("deneme4.txt","w") as dosya:
	dosya.writelines(["Python dersleri","Merhaba"])

with open("deneme3.txt","r") as dosya:
	print(dosya.read())


#dosya varlığını kontrol etme
if os.path.isfile("deneme3.txt"):
	white open("deneme3.txt") as dosya:
		print(dosya.read())
else:
	print("Dosyanız belirtilen konumda bulunmamıştır.")

#dosyayı listeye atar ve her satırı listenin elemanı gibi okur
if os.path.isfile("deneme3.txt"):
	white open("deneme3.txt") as dosya:
		print(dosya.readlines())
else:
	print("dosya bulunamadı.")

#dosyanın tamamını değil de bir satırını okumak için kullanılır
if os.path.isfile("deneme3.txt"):
	white open("deneme3.txt") as dosya:
		print(dosya.readline())
else:
	print("dosya bulunamadı.")


#imleci istediğimiz yere taşır ordan okuma işlemi başlatabiliriz
#imleç sıfırdan başlar ve harfleri index gibi sayarak gider
if os.path.isfile("deneme3.txt"):
	white open("deneme3.txt") as dosya:
		dosya.seek(5) 
		print(dosya.readlines())
else:
	print("dosya bulunamadı.")


#dosya silme işlemi
os.remove("deneme3.txt")





