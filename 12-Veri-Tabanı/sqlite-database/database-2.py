import os
import sqlite3 
veritabani = 'kitaplik.sqlite'
dosya_mevcut = os.path.exists(veritabani)

vt = sqlite3.connect(veritabani)
imlec = vt.cursor()

imlec.execute("SELECT * FROM kitap_bilgisi")
kitaplar = imlec.fetchall()
print(kitaplar)
#print(kitaplar[0])
#print(kitaplar[9])
a=1
for i in kitaplar:
    #print(i)
    print(a," ",end="")
    for k in i:
        print(k,end=" ")
    print("")
    a=a+1

vt.close()

