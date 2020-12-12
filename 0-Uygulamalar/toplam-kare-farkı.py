def KareToplam(sayi):
    toplam = 0
    for n in range(sayi+1):
        toplam += n**2
    return toplam

def ToplamKare(sayi):
    toplam = 0
    for n in range(sayi+1):
        toplam += n
    return toplam**2

print(ToplamKare(10),KareToplam(10),ToplamKare(10)-KareToplam(10))