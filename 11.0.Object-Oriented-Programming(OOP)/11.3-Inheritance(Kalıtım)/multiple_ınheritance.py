class Anne():
    def annesi(self):
        print("annesinden huyunu aldı")

class Baba():
    def babasi(self):
        print("basından huyunu aldı")

class cocuk(anne,baba):
    pass

kalıtım = cocuk()
kalıtım.annesi()
kalıtım.babasi()