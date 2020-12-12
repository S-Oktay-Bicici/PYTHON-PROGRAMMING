
def topla(a,b):
	return a+b
print(topla(3,5))

topla = lambda a,b:a+b
print(topla(3,5))

ortalama = lambda vize,final:vize*0.4+final*0.6
print(ortalama(84,75))

liste = [1,2,3,4,5]
liste2 = [i*3 for i in liste]
print(liste2)

#liste içindeki verileri for döngüsü kullanarak 3 ile çarptık
#buna list comprehesion denir.
#lamda fonksiyonuna benzer
