import os

kitapListe = list()

menu = """
 
	[1] Kitap Ekle 
	[2] Kitap Al
	[3] Tümünü Listele
	[Q] Çıkış

"""

def kitapEkle(kitap:tuple,liste:list):
	liste.append(kitap)
	print("Ekleme işlemi tamamlandı..")
	print("Ana menüye dönmek için 'enter'a basınız")
	input()


def kontrol(kitap:tuple,liste:list):
	if kitap in liste:
		return True
	else:
		return False

def kitapAl(kitap:tuple,liste:list):
	if kontrol(kitap,liste):
		liste.remove(kitap)
		print("Kitap çıkarma işlemi tamamlandı..")
		print("Ana menüye dönmek için 'enter'a basınız")
		input()
	else:
		print("Aradığınız kitap kütüphanede mevcut değildir..")
		print("Ana menüye dönmek için 'enter'a basınız")
		input()

def listele(liste:list):
	for i in liste:
		print("Kitap adı : {}  ----> Kitap yazarı : {} "format(i[0],i[1]))
	print("Ana menüye dönmek için 'enter'a basınız")
	input()

while True:
	os.system("clear") #windows için ("cls") ---> teminali temizler
	print(menu)
	
	secim = input("İşleminizi seçiniz : ")
	
	if secim == "1":
		kitap_isim = input("Kitabın ismini giriniz : ")
		kitap_yazar = input("Kitabın yazarını giriniz : ")
		kitap = (kitap_isim,kitap_yazar)
		kitapEkle(kitap,kitapListe) # kitap ekleniyor..
	elif secim == "2":
		kitap_isim = input("Kitabın ismini giriniz : ")
		kitap_yazar = input("Kitabın yazarını giriniz : ")
		kitap = (kitap_isim,kitap_yazar)
		kitapAl(kitap,kitapListe)
	elif secim == "3":
		listele(kitapListe)
	elif secim == "q" or secim == "Q":
		print("Keyifli okumalar...")
		quit()
	else:
		print("Hatalı bir işlem gerçekleştirdiniz.")
