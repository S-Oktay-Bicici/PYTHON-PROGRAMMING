#bir sayı, eğer 4 basamaklı ise ve o sayıyı
#oluşturan rakamlardan
#her birinin 4. kuvveti toplamı o sayıya eşitse bu sayı
# armstrong sayısı denir

def armstrong(sayi):
    toplam  = 0
    for rakam in str(sayi):
        toplam += int (rakam)**4
    if toplam == sayi:
        return True
    else:
        return False

for n in range(1000,10000):
    if armstrong(n):
        print(n,end='')