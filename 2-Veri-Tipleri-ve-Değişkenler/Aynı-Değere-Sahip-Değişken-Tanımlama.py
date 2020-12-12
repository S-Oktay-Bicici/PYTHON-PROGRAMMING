a = b = 4 

print(a)
print(b)

ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31 
nisan = haziran = eylül = kasım = 30
şubat = 28 

print(" ocak ayı : " ,ocak, "gün")
print(" şubat ayı : ",şubat, "gün")
print(" mart ayı : ",mart, "gün")
print(" nisan ayı : ",nisan, "gün")
print(" mayıs ayı : ",mayıs, "gün")
print(" haziran ayı : ",haziran, "gün")
print(" temmuz ayı : ",temmuz, "gün")
print(" ağustos ayı : ",ağustos, "gün")
print(" eylül ayı : ",eylül, "gün")
print(" ekim ayı : ",ekim, "gün")
print(" kasım ayı : ",kasım, "gün")
print(" aralık ayı : ",aralık, "gün")

aylık_sarfiyat = 346
fatura_tutarı = 273.87

birim_fiyat = fatura_tutarı / aylık_sarfiyat
print(birim_fiyat)

günlük_sarfiyat = aylık_sarfiyat / mart
print(günlük_sarfiyat)

nisan_faturası = birim_fiyat * günlük_sarfiyat * nisan
print(nisan_faturası)

şubat_faturası = birim_fiyat * günlük_sarfiyat * şubat 
print(şubat_faturası)
