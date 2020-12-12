#kendisi dışında bütün pozitif bölenlerinin toplamı kendisine 
#eşit olan sayılara mükemmel sayı denir

def mukemmel(sayi):
    toplam = 0

    for bolen in rangef(2,(sayi//2)+1):
        if sayi%bolen == 0:
            toplam += bolen 
        
    if toplam == sayi:
        return True
    else:
        return False

for n in range(2,1000):
    if mukemmel(n):
        print(n,end ='-')