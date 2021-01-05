class Ogretmen:
    def __init__(self,isim,soyisim,yas,maas,uzmanlık):
        self.Isim = isim
        self.Soyisim = soyisim
        self.Yas = yas
        self.__Maas = maas
        self.Uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmenidir.",format(self.Isim,self.Soyisim,self.Yas,self.Maas,self.Uzmanlık))

    def __zam(self):
        return self.__Maas * 1.3

    def getMaas(self):
        return self.__Maas
    def setMaas(self,yeni_maas):
        self.__Maas = yeni_maas

ali = Ogretmen("Ali","Salız",48,6000,"Coğrafya")


# print(self.__Maas) #hata verecektir.

print(ali.getMaas())
ali.setMaas(70000)
print(ali.getMaas())
