import tkinter as tk
from tkinter import ttk 

window = tk.Tk() # high level window

## frame
# önce sol kısma ardından sağ kımsam bir frame ekliyourz boyutlandırıyoruz
# ardından sol frame'e frame1 ve frame2 ekliyoruz
# en son olarak frame2 ye label ekliyrouz

#frame_left = tk.Frame(window, width = 540, height = 640,bg = "red")
#frame_left.grid(row = 0, column = 0, padx = 10, pady = 10)
#
#frame_right = tk.Frame(window, width = 540, height = 640, bg = "green")
#frame_right.grid(row = 0, column = 1, padx = 10, pady = 10)
#
#frame1 = tk.LabelFrame(frame_left, text =  "frame1", width = 540, height = 500,bg = "yellow")
#frame1.grid(row = 0, column = 0, padx = 10, pady = 10)
#
#frame2 = tk.LabelFrame(frame_left, text =  "frame2", width = 540, height = 140,bg = "yellow")
#frame2.grid(row = 1, column = 0, padx = 10, pady = 10)
#
#label1 = tk.Label(frame2, text="label in frame2")
#label1.grid(row=1,column=0, padx = 10, pady = 10)

# paned window
# 2 kısmı ayrılı Horizontal(yatay) ve Vertical(dikey)
# bu kısımda horizontal bir window oluşturup önce m2 yi sonra frame1 ekliyoruz
# m2 vertical ve onun da içine frame2 ve frame3 ekliyoruz

pw = ttk.Panedwindow(window, orient = tk.HORIZONTAL)
pw.pack(fill = tk.BOTH, expand = True)

m2 = ttk.Panedwindow(pw, orient = tk. VERTICAL)

frame2 = ttk.Frame(pw, width = 720, height = 400, relief = tk.RIDGE)
frame3 = ttk.Frame(pw, width = 720, height = 240, relief = tk.RAISED)
m2.add(frame2)
m2.add(frame3)

frame1 = ttk.Frame(pw, width = 360, height = 640, relief = tk.GROOVE)
pw.add(m2)
pw.add(frame1)



window.mainloop()