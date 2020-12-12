##########################################################################3

#gireceğimiz harf veya kelimeleri tek tırnak 
#yada çift tırnak ile de girebiliriz
isim = 'Oktay'
soyİsim = "BİÇİCİ"
#############################################################################

#kelimeleri arka arkaya yarken bu şekilde yazarsak
#arda boşluk bırakmadan yazacaktır
tam_isim = 'sadık' + "oktay" + "BİÇİCİ"

#############################################################################

#kelimeri ekrana basarken aralarında boşluk olması için bu şekilde yazıyoruz
tam_isim2 = "Sadık" + " " + "Oktay" + " " + "BİÇİCİ"

########################################################################

#sayıları ve simgeleri de string değeri olarak alıp ekrana yazdırmakda
deneme = "&5%*"

################################################################

print(isim)
print(soyİsim)
print(" Benim ismim :",isim , "soy ismim : ", soyİsim)
print(tam_isim)
print(tam_isim2)
print(deneme)

###########################################################

#bu şekilde de ekrana yazabiliriz
print("Sadık Oktay BİÇİCİ")

#############################################################

#bu işlem ile ismi 3 kere ekrana bastırıyotuz
print(isim*3)

############################################################

print("uzak" + " " * 5 + "çok uzak...")

##############################################################

#burda isim değerinin tipini bastırıyoruz
print(type(isim))                           #type() methodu

################################################################

#girilen karakterin uzunluğunu verir
print(len(isim))                            # len() methodu

######################################################################

a = "oktay"

print(a[0])
print(a[1])
print(a[2])  # harf harf yazdırma işlemi
print(a[3])
print(a[4])

####################################################################

a = "oktay"

print(a[-1])
print(a[-2])
print(a[-3])   # tersten harf harf yazdırma işlemi
print(a[-4])
print(a[-5])

######################################################################


b = "oktay python notları"

print(b[4:7]) #4. indeksten 7. indekse kadar basar 7. indks dahil değil

#######################################################################

b = "oktay python notları"

print(b[4:18:3]) #4. indekten 18. indekse kadar basar 18. indeks dahil değil 
                 #3 er 3er atlayarak gelir
                 
############################################################################

b = "oktay python notları"

print(b[ :4])  #başlangıç değeri verilmediyse 0. indekten başlar

############################################################################,

b = "oktay python notları"

print(b[4: ])  # bitiş değeri belirtilmediyse son değere kadar gider 

############################################################################

b = "oktay python notları"

print(b[-1])  #son karaktere  kadar alır son karakter hariç 

###########################################################################

b = "oktay python notları"

print(b[-4])  #son 4 karakteri almaz 

####################################################################

b = "oktay python notları"

print([:]])  #bütün string değerlerini alıtr

############################################################################

b = "oktay python notları"

print(b[::3])  #baştan sona 3er 3er atlayarak alır

##########################################################################

