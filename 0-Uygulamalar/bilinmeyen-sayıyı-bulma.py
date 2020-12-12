# SADIK OKTAY BİÇİCİ 1180505018

import math

def secim(a):
    #diziyi tarayarak bilinmeyen sayıyının konumunu buluyoruz
    yer = a.index('?')
    
    #bilinmeyen sayıyı '0' index de olduğunu kabul ederek işleme başlıyoruz
    if(yer == 0):
        #indexlerdeki değerleri değişkenlere atıyoruz işlemleri kolaylaştırmak için
        #karesel sayı dizisi için math kütüphanesinden sqrt fonksiyonu ile karekökünü alıyoruz
        y = int(a[1])
        y1 = math.sqrt(abs(y))
        z = int(a[2])
        z1 = math.sqrt(abs(z))
        t = int(a[3])
        t1 = math.sqrt(abs(t))

        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[1] index ile [2] indexin farkının, [2] ve [3] farkının eşitliğine bakıyoruz.
        #[3] index ile [2] indexin farkının, [2] ve [1] farkının eşitliğine bakıyoruz.
        if((y - z == z - t)  or  (t - z == z - y)):
            print("Dizi aritmetik sayı dizisidir.")
            k = (t - z)
            l = (y - k)
            print("Bilinmeyen sayının değeri: ",l)
        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[1] index ile [2] indexin bölümünün, [2] ve [3] bölümünün eşitliğine bakıyoruz.
        #[3] index ile [2] indexin bölümünün, [2] ve [1] bölümünün eşitliğine bakıyoruz.
        elif((y / z == z / t)  or (t / z == z / y)):
            print("Dizi geometrik sayı dizisidir.")
            k = (y / z)
            l = (y * k)
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[3] index ile [2] indexin farkının, [2] ve [1] indexlerin farkının '1' fazlasının eşitliğine bakıyoruz.
        #[3] index ile [2] indexin farkının, [2] ve [1] indexlerin farkının '1' eksiğinin eşitliğine bakıyoruz.
        elif(((t - z == (z - y) + 1) or (t - z == (z - y) - 1))):
            print("Dizi üçgensel sayı dizisidir.")
            k = (z - y)
            l = (y - (k-1))
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[3] indexin karekökü ile [2] indexin karekökü farkının, 
        #[2] indexin karekökü ile [1] indexin karekökü farkının eşitliğine bakıyoruz.
        elif((t1 - z1 == z1 - y1)):
            print("Dizi karesel sayı dizisidir.")
            k = (z1 - y1)
            l = (y1 - k)
            l = l*l
            print("Bilinmeyen sayının değeri: ",l)
        else:
            print("Verilen dizi bilinen aritmetik sayı dizilerine uymamaktadır.")

    #bilinmeyen sayıyı '1' index de olduğunu kabul ederek işleme başlıyoruz
    elif(yer == 1):
        x = int(a[0])
        x1 = math.sqrt(abs(x))
        z = int(a[2])
        z1 = math.sqrt(abs(z))
        t = int(a[3])
        t1 = math.sqrt(abs(t))

        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[3] index ile [2] indexin farkının 2 katı ile [2] ve [0] indexlerin farkının eşitliğine bakıyoruz.
        #[2] index ile [3] indexin farkının 2 katı ile [0] ve [2] indexlerin farkının eşitliğine bakıyoruz.
        if(((t - z)*2 == z - x)  or  ((z - t)*2 == x - z)):
            print("Dizi aritmetik sayı dizisidir.")
            k = (t - z)
            l = (x + k)
            print("Bilinmeyen sayının değeri: ",l)
        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[2] index ile [0] indexin bölümü ile [3] ve [2] indexlerin bölümünün karesinin eşitliğine bakıyoruz.
        #[2] ve [3] indexlerin bölümünün karesi ile [0] index ile [1] indexin bölümünün eşitliğine bakıyoruz.
        elif(((z / x == (t / z)*(t / z))  or ((z / t)*(z / t) == x / z))):
            print("Dizi geometrik sayı dizisidir.")
            k = (z / t)
            l = (z * k)
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[2] index ile [0] indexin farkının [3] ve [2] indexlerin farkının farkı ile
        #[3] index ile [2] indexin farkının - 3 eksiğinin eşitliğine bakıyoruz
        elif((z - x) - (t - z) == (t - z) - 3):
            print("Dizi üçgensel sayı dizisidir.")
            k = (t - z)
            l = (z - (k-1))
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[3] indexin karekökü ile [2] indexin karekökü farkının 2 katı ile  
        #[2] indexin karekökü ile [0] indexin karekökünün eşitliğine bakıyoruz
        elif((2*(t1 - z1) == z1 - x1)):
            print("Dizi karesel sayı dizisidir.")
            k = (t1 - z1)
            l = (z1 - k)
            l = l*l
            print("Bilinmeyen sayının değeri: ",l)
        else:
            print("Verilen dizi bilinen aritmetik sayı dizilerine uymamaktadır.")
            
    #bilinmeyen sayıyı '2' index de olduğunu kabul ederek işleme başlıyoruz
    elif(yer == 2):
        x = int(a[0])
        x1 = math.sqrt(abs(x))
        y = int(a[1])
        y1 = math.sqrt(abs(y))
        t = int(a[3])
        t1 = math.sqrt(abs(t))

        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[1] index ile [0] indexin 2 katı ile [3] ve [1] indexlerin farkının eşitliğine bakıyoruz.
        #[0] index ile [1] indexin 2 katı ile [1] ve [3] indexlerin farkının eşitliğine bakıyoruz.
        if(((y - x)*2 == (t - y))  or  ((x - y)*2 == (y - t))):
            print("Dizi aritmetik sayı dizisidir.")
            k = (y - x)
            l = (y + k)
            print("Bilinmeyen sayının değeri: ",l)
        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[3] index ile [1] indexin bölümü ile [1] indexi ve [0] indexi bölümünün karesinin eşitliğine bakıyoruz.
        #[0] index ve [1] index bölümünün karesi ile [1] index ile [3] indexin bölümünün eşitliğine bakıyoruz.
        elif(((t / y == (y / x)*(y / x))  or ((x / y)*(x / y) == y / t))):
            print("Dizi geometrik sayı dizisidir.")
            k = (x / y)
            l = (y * (1/k))
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[3] index ile [1] indexin farkının [1] ve [2] indexlerin farkının farkı ile
        #[1] index ile [0] indexin farkının '3' fazlasının eşitliğine bakıyoruz
        elif((t - y) - (y - x) == (y - x) + 3):
            print("Dizi üçgensel sayı dizisidir.")
            k = (y - x)
            l = (y + (k+1))
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[1] indexin karekökü ile [0] indexin karekökü farkının 2 katı ile  
        #[3] indexin karekökü ile [1] indexin karekökünün eşitliğine bakıyoruz
        elif((2*(y1 - x1) == t1 - y1)):
            print("Dizi karesel sayı dizisidir.")
            k = (y1 - x1)
            l = (y1 + k)
            l = l*l
            print("Bilinmeyen sayının değeri: ",l)
        else:
            print("Verilen dizi bilinen aritmetik sayı dizilerine uymamaktadır.")
            
    #bilinmeyen sayıyı '3' index de olduğunu kabul ederek işleme başlıyoruz
    elif(yer >= 3):
        #4 elemanı olan bir dizi için hesaplama yaptığını varsaydığımız için 
        #4 ve fazlası için bilinmeyen sayısan önceki ilk 3 elemen üzerinden 
        #sınıfını bulup bilinmeyen sayıyı bulmak için tasarlandı bu kısım
        d = yer - 3
        b = yer - 2
        c = yer - 1
        x = int(a[d])
        x1 = math.sqrt(abs(x))
        y = int(a[b])
        y1 = math.sqrt(abs(y))
        z = int(a[c])
        z1 = math.sqrt(abs(z))

        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[0] index ile [1] indexin farkını [1] ve [2] indexlerin farkının eşitliğine bakıyoruz.
        #[2] index ile [1] indexin farkını [1] ve [0] indexlerin farkının eşitliğine bakıyoruz.
        if((x - y == y - z)  or  (z - y == y - x)):
            print("Dizi aritmetik sayı dizisidir.")
            k = (z - y)
            l = (z + k)
            print("Bilinmeyen sayının değeri: ",l)
        #sayı dizisinde hem artan hem azalan olma durumu için çift yönlü kontrol ediyoruz
        #[0] index ile [1] indexin bölümüne [1] ve [2] indexlerin bölümünün eşitliğine bakıyoruz.
        #[2] index ile [1] indexin bölümüne [1] ve [0] indexlerin bölümünün eşitliğine bakıyoruz.
        elif((x / y == y / z)  or (z / y == y / x)):
            print("Dizi geometrik sayı dizisidir.")
            k = (z / y)
            l = (z * k)
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[2] index ile [1] indexin farkının [1] ve [0] indexlerinin farkının '1' fazlasının eşitliğine bakıyoruz.
        #[2] index ile [1] indexin farkının [1] ve [0] indexlerinin farkının '1' eksiğinin eşitliğine bakıyoruz.
        elif((z - y == (y - x) + 1) or (z - y == (y - x) - 1)):
            print("Dizi üçgensel sayı dizisidir.")
            k = (z - y)
            l = (z + (k+1))
            print("Bilinmeyen sayının değeri: ",l)
        #bu sayı dizisinde sadece artan olduğu için tek yönden inceliyoruz
        #[2] indexin karekökü ile [1] indexin karekökü farkının,
        #[1] indexin karekökü ile [0] indexin karekökğ karının eşitliğine bakıyoruz
        elif((z1 - y1 == y1 - x1)):
            print("Dizi karesel sayı dizisidir.")
            k = (z1 - y1)
            l = (z1 + k)
            l = l*l
            print("Bilinmeyen sayının değeri: ",l)
        else:
            print("Verilen dizi bilinen aritmetik sayı dizilerine uymamaktadır.")

    else:
        print("Yanlış bir sayı dizisi yazıldı, işlem yapılamdı.")
    

def main():
    """

    # kullanıcıdan değer almadan önce kontrol mekanizması için 
    #hazır diziler ekliyoruz ve sayı dizisine göre kullanıyoruz

    #aritmetik 
    testcase01 = [6,11,'?',21] #output: 16 
    testcase02 = [21,'?',11,6] #output: 16
    testcase03 = ['?',11,16,21] #output: 6
    testcase04 = ['?',16,11,6] #output: 21
    testcase05 = [6,11,16,'?'] #output: 21
    testcase06 = [11,6,1,'?'] #output: -4

    #geometrik
    testcase07 = [2,6,'?',54] #output: 18 
    testcase08 = [54,'?',6,2] #output: 18
    testcase09 = ['?',54,18,6] #output: 162
    testcase10 = ['?',5,25,125] #output: 1
    testcase11 = ['?',-5,5,-5] #output: 5
    testcase12 = [-5,5,-5,'?'] #output: 5
    testcase13 = [2,6,18,'?'] #output: 54
    testcase14 = [54,18,6,'?'] #output: 2

    #üçgensel
    testcase15 = ['?',15,21,28] #output: 10 
    testcase16 = [10,15,'?',28] #output: 21
    testcase17 = [10,15,21,'?'] #output: 28
    testcase18 = [10,'?',21,28] #output: 15

    #karesel
    testcase19 = ['?',4,9,16] #output: 1
    testcase20 = [1,4,'?',16] #output: 9
    testcase21 = [16,49,100,'?'] #output: 169
    testcase22 = [16,'?',36,49] #output:25

    secim(testcase18)
    """
    #kullanıcıdan aldığımız sayı diziyi
    #oluşturmuş olduğumuz diziye aktarıp metodu çağırıyoruz
    sayidizisi = []
    sd = input("Lütfen sayı dizisini aralarında virgül olacak şekilde giriniz(a,b,?,d):")
    #split metodu ile aldığımız dizi içerisindeki ',' karakterini silerek 
    #dizide yer kaplamasını önüyor ve işlemler için kolaylık sağlıyor
    sayidizisi = sd.split(',')

    secim(sayidizisi)

main()

