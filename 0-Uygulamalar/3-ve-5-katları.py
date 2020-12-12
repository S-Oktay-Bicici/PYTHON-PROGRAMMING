toplam = 0
for sayi in range(1000):
    if sayi % 3 == 0 or sayi % 5 == 0:
        toplam = sayi + toplam

print(toplam)