# ### Öğrencilerin aldıkları puanların olduğu bir listede, en yüksek puanın kaç olduğunu bulan kodu yazınız

puanlar = [54.3, 76.7, 34.1, 45, 89, 67.9]
maximum = 0

for i in range(6): # 1,2,3,4,5
    if puanlar[i] > maximum:
        maximum = puanlar[i]
print(maximum)


puanlar = [54.3, 76.7, 34.1, 45, 89, 67.9]
maximum = 0

for sayi in puanlar:
    if sayi > maximum:
        maximum = sayi
print(maximum)

