# is işleci
# id fonksiyonu

a = 5
b = 5

if a == b:
	print("aynı")

#is işleci değerlerin eşit olma durumu değil id lerin eşit olma durumuna bakar
if a is b:
	print("aynı")


# id fonkisyomu değere atanan kimliği gösteriyor
print(id(a))
print(id(b))
print(id(5))
