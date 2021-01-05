class Okul():
    def __init__(self,name,surname,age):
        self.Name = name
        self.Surname = surname
        self.Age = age

    def info(self):
        print("{} {} {} yaşında bir okul elemanıdır.")

class Ogretmen(Okul):
    def __init__(self,name,surname,age,maas,uzmanlık):
        super().__init__(name,surname,age)
        self.Maas = maas
        self.Uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaş olan bir {} öğretmenidir. ".format(self.Name,self.Surname,self.Age,self.Maas,self.Uzmanlık))


aslı = Ogretmen("Aslı","Dere",26,4000,"Edebiyat")
sedef = Ogrenci("Sedef","Kum",19,59)

aslı.info()
sedef.info()

"""
info metodu üst sınıftan kalıtım yolu ile gelse de 
kedndi sınıfındaki şekliyle kullanıldı buna overriding denir
"""