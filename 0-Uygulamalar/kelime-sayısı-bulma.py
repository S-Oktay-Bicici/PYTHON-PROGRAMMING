cumle = input("Bir cümle giriniz: )

bosluk = 0
for karakter in cumle:
    if karakter == " ":
        bosluk = bosluk+1
    
print("Kelime sayısı: ",bosluk+1)