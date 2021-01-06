from tkinter import *
from gtts import gTTS
import os

def konustur():
    metin = giris.get()
    giris.delete(0,END)

    tts = gTTS(text = metin, lang = 'tr')

    tts.save("merhaba.mp3")
    os.system("merhaba.mp3")

pencere = Tk()
pencere.geometry("375x200")

giris = Entry()
giris.pack()

dugme = Button(text = "konuştur", command = konustur)
dugme.pack()

mainloop()
