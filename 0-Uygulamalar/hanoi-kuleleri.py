from os import  system

nesne = ['|','_','___','_____','_______','_________','___________']

def yeniOyun():
    global kule
    global hareket_sayisi
    global seviye
    global taban_genisligi
    seviye = int(input("Kaç diskle oynamak istersiniz? (3,4,5,6)"))
    taban_genisligi = seviye*2+1
    hareket_sayisi = -1
    kule = [[i for i in range(seviye, 0, -1)],[],[],]
    kuleYaz()

def kuleYaz():
    global hareket_sayisi
    global seviye
    global taban_genisligi
    hareket_sayisi += 1

    system("cls")

    print("~~"*taban_genisligi*3)
    satir = ''

    for yatay in range(seviye-1, -1, -1):
        for dikey in range(3):
            try:
                satir += nesne[kule[dikey][yatay]].center(taban_genisligi)
            except:
                satir += nesne[0].center(taban_genisligi)
        print(satir)
        satir = ''

    print("~~"*taban_genisligi*3)

def oyunMotoru():
    while True:
        hareket = input("Diski nereden nereye taşımak istiyorsun: (1 3)")
        h = [int(i)-1 for i in hareket.split()]

        if len(kule[h[0]])>0:
            if len(kule[h[1]])>0:
                if kule[h[0]][-1] < kule[h[1]][-1]:
                    kule[h[1]].append(kule[h[0]][-1])
                    kule[h[0]].pop()
                    kuleYaz()
                else:
                    print("Disk taşımak için fazla büyük!")
            else:
                kule[h[1]].append(kule[h[0]][-1])
                kule[h[0]].pop()
                kuleYaz()
        else:
            print("Taşınacak disk yok!")
        
        if len(kule[2]) == seviye:
            print("Tebrikler!",hareket_sayisi,"hamlede bitirdiniz.")
            break

while True:
    yeniOyun()
    oyunMotoru()

    if input("Yeniden oynamak ister misiniz ? (e,h)") != "e":
        break