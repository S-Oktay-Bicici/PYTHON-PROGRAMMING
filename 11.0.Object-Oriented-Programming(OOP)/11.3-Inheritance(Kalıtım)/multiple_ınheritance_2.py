class Anne():
    def __init__(self):
        self.sac="kıvırcık"
        print(self.sac)

    def göz(self):
        self.göz="mavi"
        pritn(self.göz)

class Baba():
    def __init__(self):
        self.sac="düz"
        print(self.sac)

    def göz(self):
        self.göz="yeşil"
        pritn(self.göz)

class Cocuk(anne,baba):
    def __init__(self):
        baba.__init__(self)

kalıtım = Cocuk()
kalıtım.göz

"""
kalıtım yapırlacak sınıfların veriliş sırası önemlidir
farklı bir durum belirtilmediği sürece ilk verilen sınıftan kalırım gerçekleşir
bu durumda cocuk sınıfda constructor metodu babanın consructor metodunu kullanmayı mecbur kıldığından 
babanın construcor metrodu kullanıclacak fakat ilk anne belirtildiği için göz metodunda anneden alıcaktır.
"""