
a,b = 0,1
i = 1
sınır = int(input("seri sınırını giriniz : "))

while(i<sınır):
	a,b =b,a+b
	print(b)
	i+=1

#################################################################

a,b = 0,1
fibonacci = [a,b]

for i in range(20):
	a,b = b,a+b
	fibonacci.append(b)

print("fibonacci serisi : ",fibonacci)
