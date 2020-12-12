# ### Verilen iki Dictionary yapısındaki elemanları tek bir Dictionary'e çeviren, eğer ortak elemanlar varsa değerlerini toplayarak tek bir eleman şeklinde yazan kodu yazınız
# 
# ##### Örnek: d1 = {"a":2, "b":6, "d":3, "g":1}
# #####             d2 = {"b":1, "c":4, "e":8, "f":1, "g":7}
# ##### Sonuç: d3 = {"a":2, "b":7, "c":4, "d":3, "e":8, "f":1, "g":8}

d1 = {"a":2, "b":6, "d":3, "g":1}
d2 = {"b":1, "c":4, "e":8, "f":1, "g":7}
d3 = {}


for item in d1:
    if item in d2:
        d3[item] = d1[item] + d2[item]
    else:
        d3[item] = d1[item]
for item in d2:
    if item not in d3:
        d3[item] = d2[item]
print(d3)

