#bir excel çalışma sayfasının sütun başlığı verildiğinde,
#karşılık gelen sütun numarasını hesaplayan bir fonksiyon

def sutunno(sutun):
    sutun = sutun.upper()
    ussu = len(sutun)-1

    toplam = 0
    for harf in sutun:
        toplam += (26**ussu)*(ord(harf)-ord('A')+1)
        ussu -= 1
    
    return toplam

for n in range(5):
    print(sutunno(input("Sütün başlığını giriniz: ")))
