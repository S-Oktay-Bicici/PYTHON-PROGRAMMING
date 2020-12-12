
liste = [1,2,65.53,"oktay","biçici"]
print(liste)
print(len(liste))

liste2 = [1,2,65.53,["iç içe",29],"oktay","biçici"]
print(liste2)
print(len(liste2))

a = "sadık"
print(type(a))
print(a)

b = list(a)
print(b)
print(type(b))

##################################################################

a = "oktay"
b = list(a)

print(b[0])
print(b[1])
print(b[2])  # harf harf yazdırma işlemi
print(b[3])
print(b[4])

####################################################################

a = "oktay"
b = list(a)

print(b[-1])
print(b[-2])
print(b[-3])   # tersten harf harf yazdırma işlemi
print(b[-4])
print(b[-5])

######################################################################

liste = [1,2,65.53,"oktay","biçici"]
print(liste[2])

#######################################################################

liste = [1,2,65.53,"oktay","biçici"]
print(liste[0])

#######################################################################

liste = [1,2,65.53,"oktay","biçici"]
print(liste[-1])
#son değer yazdırılır

#######################################################################

liste = [1,2,65.53,"oktay","biçici"]
print(liste[-2])
#sondan bie önceki yazdırılıcak

#######################################################################

liste = [1,2,65.53,["iç içe",29],"oktay","biçici"]
print(liste[3][1])
#listenin içindeki listeye erişim sağlıyoruz ve içerdeki listenin 
#ilk elemanını bastırıyoruz

#######################################################################

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(liste[6][1])
#listenin içindeki listeye erişim sağlıyoruz ve içerdeki 2. listenin 
#ilk elemanını bastırıyoruz

#######################################################################

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(liste[1:6])
 #1. indeksten 6. indekse kadar basar 6. indks dahil değil

#######################################################################

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(b[1:6:2]) 
#1. indekten 6. indekse kadar basar 6. indeks dahil değil 
#2şer 2şer atlayarak gelir
                 
############################################################################

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(liste[1:]) 
# bitiş değeri belirtilmediyse son değere kadar gider 

############################################################################

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(liste[:5])
#başlangıç değeri verilmediyse 0. indekten başlar

############################################################################,

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(liste[::2]) 
#son karaktere  kadar 2şer 2şer alır 

###########################################################################

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(liste[len(liste)-1]) 
#listenin sonuncu elemanının yazdırmış oluruz

####################################################################

liste = [1,2,65.53,["iç içe",29],"sadık",["oktay","biçici"],"python"]
print(b[::-1])
#listeyi tersten yazdırırız

############################################################################

liste = [1,2,65.53,["iç içe",29]
liste1 = ["sadık",["oktay","biçici"],"python"]
b = liste + liste1
print(b)

##########################################################################

liste = [1,2,65.53,["iç içe",29]
liste1 = ["sadık",["oktay","biçici"],"python"]
print(liste+liste1)

#########################################################################

liste = [1,2,65.53,["iç içe",29]
liste1 = ["sadık",["oktay","biçici"],"python"]
print(liste+liste1+["notları"])

#########################################################################

liste = [1,2,65.53,["iç içe",29]
liste1 = ["sadık",["oktay","biçici"],"python"]
print(liste+liste1*2)

#######################################################################3
