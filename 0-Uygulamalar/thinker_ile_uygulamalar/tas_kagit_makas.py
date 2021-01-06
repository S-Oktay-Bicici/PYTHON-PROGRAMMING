from tkinter import *
import random
import time

def tas():
    global oyuncuSecim
    oyuncuSecim = 'taş'
    kiyasla()
def kagit():
    global oyuncuSecim
    oyuncuSecim = 'kağıt'
    kiyasla()
def makas():
    global oyuncuSecim
    oyuncuSecim = 'makas'
    kiyasla()

def kiyasla():
    global liste
    global skorOyuncu
    global skorBilgisayar
    global oyuncuSecim
    random.shuffle(liste)
    time.sleep(0.3)
    if liste[0]==oyuncuSecim:
        secimBilgisayar['text']="Bilgisayarın Seçimi: "+liste[0]
        
    elif liste[0]=='taş' and oyuncuSecim == 'makas':
        secimBilgisayar['text']="Bilgisayarın Seçimi: "+liste[0]
        skorBilgisayar += 1
        puanBilgisayar['text']='Bilgisayar: '+str(skorBilgisayar)
    elif liste[0]=='taş' and oyuncuSecim == 'kağıt':
        secimBilgisayar['text']="Bilgisayarın Seçimi: "+liste[0]
        skorOyuncu += 1
        puanOyuncu['text']='Oyuncu: '+str(skorOyuncu)
    elif liste[0]=='makas' and oyuncuSecim == 'kağıt':
        secimBilgisayar['text']="Bilgisayarın Seçimi: "+liste[0]
        skorBilgisayar += 1
        puanBilgisayar['text']='Bilgisayar: '+str(skorBilgisayar)
    elif liste[0]=='makas' and oyuncuSecim == 'taş':
        secimBilgisayar['text']="Bilgisayarın Seçimi: "+liste[0]
        skorOyuncu += 1
        puanOyuncu['text']='Oyuncu: '+str(skorOyuncu)
    elif liste[0]=='kağıt' and oyuncuSecim == 'taş':
        secimBilgisayar['text']="Bilgisayarın Seçimi: "+liste[0]
        skorBilgisayar += 1
        puanBilgisayar['text']='Bilgisayar: '+str(skorBilgisayar)
    elif liste[0]=='kağıt' and oyuncuSecim == 'makas':
        secimBilgisayar['text']="Bilgisayarın Seçimi: "+liste[0]
        skorOyuncu += 1
        puanOyuncu['text']='Oyuncu: '+str(skorOyuncu)
   
        

    
liste = ['taş','kağıt','makas']
skorOyuncu = 0
skorBilgisayar = 0
                   
pencere = Tk()
pencere.title("Taş Kağıt Makas")
pencere.config(bg = 'black')

genislik = pencere.winfo_screenwidth()//2
yukseklik = pencere.winfo_screenheight()//2
pencere.geometry("{}x{}+300+200".format(genislik,yukseklik))
puanOyuncu = Label(pencere,fg = 'red', font = 'Comic 15 bold',
                       bg = 'black', text = "Oyuncu : 0")
puanOyuncu.place(x = 10, y = 50)

puanBilgisayar = Label(pencere,fg = 'red', font = 'Comic 15 bold',
                           bg = 'black',text = "Bilgisayar : 0")
puanBilgisayar.place(x = 350, y = 50)

secimBilgisayar = Label(pencere,fg = 'red', font = 'Comic 15 bold',
                           bg = 'black',text = "Bilgisayarın Seçimi: ")
secimBilgisayar.place(x = 200, y = 120)

dugmeTas = Button(pencere,text = 'Taş', command = tas, width = 7)
dugmeKagit = Button(pencere,text = 'Kağıt', command = kagit, width = 7)
dugmeMakas = Button(pencere,text = 'Makas', command = makas, width = 7)

dugmeTas.place(x = 50,y = 150)
dugmeKagit.place(x = 50,y = 200)
dugmeMakas.place(x = 50,y = 250)
pencere.mainloop()


