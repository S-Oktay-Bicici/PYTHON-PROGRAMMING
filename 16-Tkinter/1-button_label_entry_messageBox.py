import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk() # 
window.geometry("500x450") # ekran boyutların ayarlıyoruz
window.title("Welcome to first app") # başlık ekliyoruz 

def buttonFunction():
    print("Push button")
    
    # label butona basılması durumunda label içeriğini değiştiriyoruz 
    label.config(text = "hello world",
                 fg = "black",
                 bg = "red",
                 font = "Times 25")
    
    # entry yazılan değerleri value değeerine atıyrouz ve label üzerinde yazdırıyoruz
    value = entry.get()
    print(value)
    label.configure(text = value)
    # yazıyı yazdırdıktan sonra yazı yazılmasını engelliyoruz
    entry.configure(state = "disabled")

    # message boxlar ile ilgili bir kaç çeşit örnek yazdık
#    message_box = messagebox.showinfo(title = "info", message = "information")
#    message_box = messagebox.askretrycancel(title = "info", message = "information")
#    message_box = messagebox.askquestion(title = "info", message = "information")
#    message_box = messagebox.askyesnocancel(title = "info", message = "information")
    message_box = messagebox.showerror(title = "info", message = "information")
    print(message_box)
    
# button özellikleri belirliyoruz sırası ile 
# ilk olarak çıkmasını istediğimiz ekranı tercih ediyoruz 
# buton üzerineki yazıyı belirliyourz ve renkleri ardından boyutunu 
# son olarak basıldığında yapmasını istediğmiz işlevleri yazdığımız fonksiyona yönlendiriyoruz
button = tk.Button(window, text = "First button", activebackground = "red",
                   bg = "black", fg = "white", activeforeground = "black",
                   height = 15, width = 50,
                   command = buttonFunction)

button.pack() #oluşturduğumuz butonu ekranda gözükmesini sağlıyoruz

# label özelliklerini belirliyouruz 
label = tk.Label(window, text = "Hi World", font = "Times 16", fg = "white", bg = "black",
                 wraplength = 150)

# ekran içerisinde gözükmesini ve konumunu ayarlııyoruz
label.pack(side = tk.RIGHT, padx = 25)

# entry oluşturudk ve içerisine yazı yazdık, ekranın neresinde olacağına karar verdik
entry = tk.Entry(window, width = 50)
entry.insert(string = "haydi yaz yaz yaz",index = 0)
entry.pack(side = tk.LEFT, padx = 25)


window.mainloop() # tasarlamış olduğumuz ekranı görüntüleme işlemi