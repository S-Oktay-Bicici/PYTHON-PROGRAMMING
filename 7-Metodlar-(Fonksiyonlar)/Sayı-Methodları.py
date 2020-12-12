
"""

	bit_length()   ---> bit uzunluğu

"""

sayı = 5
print(sayı.bit_length())


"""

	as_integer_ratio() --->bölüm sonucu çıkması için gereken tam sayıları verir
	is_integer()  ---> sayı tam sayı ise True döndürür

"""

sayı = 4.5
print(sayı.as_integer_ratio())

sayı = 4.0
print(type(sayı))
print(sayı.is_integer())

"""

	imag ---> complex sayıların sanal kısmını verir
	real ---> complex sayıların gerçek kısmını verir

"""

karmaşık = 12+4j
print(type(karmaşık))
print(karmaşık.imag)
print(karmaşık.real)

"""

	abs()     ---> Mutlak değer olarak döndürür
	divmod()  ---> Bölüm ve kalanı verir
	max()     ---> Max değer bulunur
	min()     ---> Min değer bulunur
	sum()     ---> Dizi içindeki tüm sayıları toplar

"""

print(abs(-8))
print(divmod(39,12))

liste = [1,2,3,4,5]
print(max(liste))
print(min(liste))

liste1 = ["sadık","oktay","biçici","abdullah"]
print(max(liste1,key=len))

print(sum(liste))
print(sum(liste,5))
