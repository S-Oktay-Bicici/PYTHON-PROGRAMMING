class Ogrenci():
    def __init__(self,isim,soyisim,yas,not_ort):
        self.Name = isim
        self.Soyisim = soyisim
        self.Yas = yas
        self.Not = not_ort

    def info(self):
        print("{} {} {} yaşında ve {} not orlamasına sahip.".format(self.Name,self.Soyisim,self.Yas,self.Not))
        
bir = Ogrenci("mehmet", "tek",18,43)
iki = Ogrenci("ali","sakız",28,65)

bir.info()
iki.info()
