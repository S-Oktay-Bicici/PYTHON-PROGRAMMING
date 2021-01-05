class Okul():
    def __init__(self,name,surname,age,maas):
        self.Name = name
        self.Surname = surname
        self.Age = age
        self.Maas = maas

    def info(self):
        print("{} {} {} yaşında bir okul elemanıdır.")

    def zam(self):
        return self.Maas * 1.2

class Ogretmen(Okul):
    def __init__(self,name,surname,age,maas,uzmanlık):
        super().__init__(name,surname,age,maas)
        self.Uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaş olan bir {} öğretmenidir. ".format(self.Name,self.Surname,self.Age,self.Maas,self.Uzmanlık))

    def zam(self):
        return self.Maas * 1.5

class Yonetim(Okul):
    def __init__(self,name,surname,age,maas,birim):
        super().__init__(name,surname,age,maas)
        self.Birim = birim

    def info(self):
        print("{} {} {} yaşında ve {} maaş olan bir {} bir yönetim elemanıdır. ".format(self.Name,self.Surname,self.Age,self.Maas,self.Birim))
        
    def zam(self):
        return self.Maas * 2

class Hizmetli(Okul):
    def __init__(self,name,surname,age,maas):
        super().__init__(name,surname,age,maas)

    def info(self):
        print("{} {} {} yaşında ve {} maaş olan bir {} bir hizmet elemanıdır. ".format(self.Name,self.Surname,self.Age,self.Maas))
        
    def zam(self):
        return self.Maas * 3

mehmet = Okul("mehmet","korkmaz",45,4000)
ali = Ogretmen("ali","kırık",35,4000,"Matematik")
fatma = Yonetim("fatma","dere",36,4000,"Müdür yardımcısı")
deniz = Hizmetli("deniz","deniz",35,4000)

print(mehmet.zam())
print(ali.zam())
print(fatma.zam())
print(deniz.zam())