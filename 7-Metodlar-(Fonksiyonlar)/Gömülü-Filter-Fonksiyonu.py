
liste = [1,2,3,4,5]
filter1 = filter(lambda sayı:sayı%2==0,liste)
print(filter1)


liste = [1,2,3,4,5]
filter1 = filter(lambda sayı:sayı%2==0,liste)
print(list(filter1))

liste = range(50)
filter1 = filter(lambda sayı:sayı%2==0,liste)
print(list(filter1))

liste = range(50)

def asal_sayı(sayı):
	i=2
	if(sayı==2):
		return True
	elif sayı<2:
		return False
	else:
		while(i<sayi):
			if(sayı%i==0):
				return False
			i+=1
			return True
filter2 = filter(asal_sayı,liste)
print(list(filter2))
