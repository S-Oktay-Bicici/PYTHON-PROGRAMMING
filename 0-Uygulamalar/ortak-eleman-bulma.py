# ### İki listedeki ortak elemanları bulan ve bu ortak elemanları yeni bir listeye ekleyen kodu yazınız

l1 = [3, 5, 6, 7, 9, 11]
l2 = [1, 2, 3, 6, 8, 9, 14]


l3 = []
for item in l1:
    if item in l2:
        l3.insert(0, item)
print(l3)

