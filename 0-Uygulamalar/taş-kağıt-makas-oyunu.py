from random import randint
from time import sleep,strftime

tkm = {1:"Taş", 2:"Kağıt", 3:"Makas"}

while True:
    pc_puan = 0
    oyuncu_puan = 0
    elsayisi = int(input("Kaç el oynamk istersiniz?"))

    for n in range(elsayisi):
        oyuncu_secim = int(input("Taş, Kağıt, Makas ? (1,2,3)"))
        pc_secim = randint(1,3)

        if(oyuncu_secim == 1 and pc_secim == 2):
            pc_puan += 1
            kazanan = "pc"
        elif(oyuncu_secim == 1 and pc_secim == 3):
            oyuncu_puan += 1
            kazanan = "oyuncu"
        elif(oyuncu_secim == 2 and pc_secim == 1):
            oyuncu_puan += 1
            kazanan = "oyuncu"
        elif(oyuncu_secim == 2 and pc_secim == 3):
            pc_puan += 1
            kazanan = "pc"
        elif(oyuncu_secim == 3 and pc_secim == 1):
            oyuncu_puan += 1
            kazanan = "oyuncu"
        elif(oyuncu_secim == 3 and pc_secim == 2):
            pc_puan += 1
            kazanan = "pc"
        else:
            kazanan = "berabere"
        
        print("PC: ",tkm[pc_secim],"Oyuncu: ",tkm[oyuncu_secim],"---->",end="")
        sleep(1)
        print(kazanan)


    if pc_puan > oyuncu_puan:
        print("Kazanan PC")
    elif pc_puan < oyuncu_puan:
        print("Kazanan oyuncu")
    else:
        print("Berabere.")

    file = open("kayitlar.txt","a")
    file.write(strftime('%c')+"-Oyunucu:"+str(oyuncu_puan)+"PC:"+str(pc_puan)+"\n")
    file.close()

    if input("Yeniden oynamak ister misiniz?") != "e":
        break