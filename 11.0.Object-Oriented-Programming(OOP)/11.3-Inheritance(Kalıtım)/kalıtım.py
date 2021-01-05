class Okul():
    def __init__(self,name,surname,age):
        self.Name = name
        self.Surname = surname
        self.Age = age

class Ogretmen(Okul):
    def __init__(self,name,surname,age,maas,uzmanlık):
        super().__init__(name,surname,age)
        self.Maas = maas
        self.Uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaş olan bir {} öğretmenidir. ".format(self.Name,self.Surname,self.Age,self.Maas,self.Uzmanlık))

    def zam(self):
        return self.Maas * 1.5

class Ogrenci(Okul):
    def __init__(self,name,surname,age,not_ort):
        super().__init__(name,surname,age)
        self.Not = not_ort

    def info(self):
        print("{} {} {} yaşında ve {} ortalamaya sahip. ".format(self.Name,self.Surname,self.Age,self.Not))
    

aslı = Ogretmen("Aslı","Dere",26,4000,"Edebiyat")
sedef = Ogrenci("Sedef","Kum",19,59)

aslı.info()
sedef.info()