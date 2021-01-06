import tkinter
import random
renkler = [["yellow","sarı"],["green","Yeşil"],["red","Kırmızı"],
           ["blue","Mavi"],["black","Siyah"],["white","Beyaz"],
           ["purple","Mor"],["pink","Penbe"],["brown","Kahverengi"],
           ["orange","Turuncu"],["navy blue","Lacivert"],["violet","Eflatun"],
           ["grey","Gri"]]

skor = 0
kalan_sure = 60

def basla(event):
    if kalan_sure == 60:
        say()
    yeni_renk()
def yeni_renk():
    global skor
    global kalan_sure

    if kalan_sure > 0:
        

        if giris.get().lower() == renkler[1][1].lower():
            skor += 1

        giris.delete(0, tkinter.END)

        random.shuffle(renkler)

        etiket.config(fg = str(renkler[1][0]), text = str(renkler[0][1]))

        skor_etiketi.config(text = "Skor: "+str(skor))

def say():
    global kalan_sure

    if kalan_sure > 0:
        kalan_sure -= 1
        sure_etiketi.config(text = "Kalan Süre: "+ str(kalan_sure))
        sure_etiketi.after(1000,say)
        

pencere = tkinter.Tk()
pencere.title('Renk Oyunu')
pencere.geometry("450x350")

aciklama = tkinter.Label(pencere, text = "Kelimelerin Rengini Gir, Kelimeyi yazma",
                         font = ('Helvetica',12))
aciklama.pack()

skor_etiketi = tkinter.Label(pencere, text = "Başlamak için enter'a bas",
                             font = ('Helvetica',12))
skor_etiketi.pack()

sure_etiketi = tkinter.Label(pencere, text = "Kalan Süre: "+ str(kalan_sure),
                             font = ('Helvetica',12))
sure_etiketi.pack()

etiket = tkinter.Label(pencere, font = ('Helvetica',60))
etiket.pack()

giris = tkinter.Entry(pencere)

pencere.bind('<Return>', basla)
giris.pack()

giris.focus_set()

pencere.mainloop()















