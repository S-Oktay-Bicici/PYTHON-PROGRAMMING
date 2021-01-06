from tkinter import *
deneme = 3
def giris():
    global deneme
    if deneme > 0:        
        if (giris1.get()=="Admin" and giris2.get()=="12345"):
            cerceve.destroy()
            etiket4 = Label(pencere, text = "Giriş Başarılı",
                           font = "Comic 20 bold", bg = 'Aqua')
            etiket4.place(x = 170, y = 170)
            dugme3 = Button(pencere, text = "Çıkış", command = pencere.destroy)
            dugme3.place(x = 300, y = 230)
        else:
            deneme -=1
            etiket3['text'] = "Giriş Bilgileri Hatalı"    
               
pencere = Tk()
pencere.title("Kullanıcı Giriş Formu")
pencere.config(bg = 'Aqua')
pencere.geometry("500x450+150+150")

cerceve = Frame(pencere, bg = 'Aqua', width = 200, height = 100)
etiket = Label(cerceve, text ='Kullanıcı Girişi', bg = 'Aqua',
          font = "Comic 20 bold")
etiket.pack(pady = 15)
etiket1 = Label(cerceve, text = "Kullanıcı Adı:", bg = "dark grey",
                width = 20)
etiket2 = Label(cerceve, text = "Parola:", bg = "dark grey",
                width = 20)
giris1 = Entry(cerceve, width = 20)
giris2 = Entry(cerceve, width = 20, show = '*')

dugme1 = Button(cerceve, text = "Giriş", width = 5, command = giris)
etiket3 = Label(cerceve, bg = 'Aqua')
cerceve.pack(pady = 80)
etiket1.pack(pady = 5)
giris1.pack(pady = 5)
etiket2.pack(pady = 5)
giris2.pack(pady = 5)
dugme1.pack(pady = 5)
etiket3.pack(pady = 5)
pencere.mainloop()
