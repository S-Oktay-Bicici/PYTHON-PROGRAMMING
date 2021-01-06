from tkinter import *
import time

def saat_goster():
    su_an = time.strftime('%H:%M:%S')
    saatEtiketi['text']=su_an
    pencere.after(1000,saat_goster)
    
    


pencere = Tk()
pencere.title('Dijital Saat')
saatEtiketi = Label(pencere,font='Times 70',bg = 'black',fg = 'dark green')
saatEtiketi.grid(row=0,column=0)
saat_goster()
mainloop()
