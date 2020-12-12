# ### Verilen key listesini ve value listesini, dictionary'e çeviren kodu yazınız

keys = ["elma", "armut", "portakal", "muz"]
values = [5, 4.5, 6, 8]


d = {}

for i in range(len(keys)):
    meyve = keys[i]
    fiyat = values[i]
    d[meyve] = fiyat
print(d["portakal"])

