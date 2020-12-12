

def toplam(*args):
	print(sum(args))
toplam(1,2)
toplam(1,2,3)
toplam(1,2,3,4)

def toplama(*python):
	print(sum(python))
toplama(1,2)
toplama(1,2,3)
toplama(1,2,3,4)

def göster(*değerler):
	print(değerler)
göster(1,2,5,8)
göster("merhaba",5.58,85,["gün","ay","yıl"],{"pazartesi","salı"})

#########################################################################

def rehber(**kwargs):
	print(kwargs)
rehber(isim = "ahmet",soyisim = "demirci")

def döviz(**para):
	print(para)
döviz(euro = 6.75,dolar = 6.34)

##########################################################################

def göster(*args,**kwargs):
	print(args)
	print(kwargs)
göster(5,8,3,7,15,"merhaba")

def göster(*args,**kwargs):
	print(args)
	print(kwargs)
göster(5,8,7,15,"merhaba",isim = "oktay",soyisim = "biçici")

def göster(**kwargs,**args):
	print(args)
	print(kwargs)
göster(5,8,7,15,"merhaba",isim = "oktay",soyisim = "biçici")

#args ve kwargs birlikte kullanılacaksa kesinlikle args önce kullanılmalı
