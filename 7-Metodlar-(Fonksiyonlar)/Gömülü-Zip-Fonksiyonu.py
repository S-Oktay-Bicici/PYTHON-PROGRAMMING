
isim = ["ahmet","mehmet","hakan"]
soyisim = ["aydın","yılmaz","kaya"]
zip1 = zip(isim,soyisim)
print(zip1)

isim = ["ahmet","mehmet","hakan"]
soyisim = ["aydın","yılmaz","kaya"]
zip1 = zip(isim,soyisim)
print(list(zip1))

liste1 = [3,5,7,8,9,10,85,95]
liste2 = [2,4,6,8,63,54,45,7]
liste3 = [45,74,87,95,78,98]

for i,j,k in zip(liste1,liste2,liste3):
	filter1 = filter(lambda i:i%3==0,liste)
	filter2 = filter(lambda j:j%5==0,liste2)
	filter3 = filter(lambda k:k%7==0,liste3)

print("3'ün katları :",list(filter1))
print("5'in katları :",list(filter2))
print("7'nin katları :",list(filter2))
