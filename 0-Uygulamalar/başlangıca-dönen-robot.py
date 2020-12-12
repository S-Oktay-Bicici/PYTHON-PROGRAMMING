# iki boyutlu bir düzlemde (0,0) konumundan harekete başlayan bir robot vardır.
#hareketleri bir karakter dizisi ile gösterilmektedir. geçerli;
#R(sağ),L(sol),U(yukarı),D(aşşağı) şeklindedir.

#buna göre hareketleri sırası ile verilen robotun, hareketlerini tamamladıktan sonra
#başlangıç noktasına dönüp dönmediğini bulan fonksiyon

# örnek "UD" , "LLURDR"

def basadondu(hareket):
    X,Y = 0,0
    hareket = hareket.upper()

    for h in hareket:
        if h == "U":
            Y += 1
        elif h == "D":
            Y -= 1
        elif h == "L":
            X -= 1
        elif h == "R":
            X += 1
        
    if X == 0 and Y == 0:
        return True
    else: 
        return False

def basadondu2(hareket):
    hareket = hareket.upper()
    if hareket.count("L") == hareket.count("R") and hareket.count("D") == hareket.count("U"):
        return True
    else:
        return False


for n in range(5):
    hareket = input("Robotun hareket dizisini giriniz: ")
    if basadondu(hareket):
        print("Robot başlangıç noktasında")
    else:
        print("Robot başlangıç noktasında değil.")