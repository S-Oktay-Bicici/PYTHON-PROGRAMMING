
"""
	==   ---> eşittir
	!=   ---> eşit değildir
	>    ---> büyüktür
	<    ---> küçüktür
	>=   ---> büyük eşittir
	<=   ---> küçük eşittir
"""

#and
print("Python" == "Python" and 2>1)
print("Ders" == "ders" and 54>=54)
print("kurs" != "ders" and 2<5 and 99>54 and "gündüz" == "gündüz")

#or
print("Python" == "Python" or 2>1)
print("Ders" == "ders" or 54>=87)
print("kurs" == "ders" or 2>5)
print("kurs" != "ders" or 2<5 or 99<54 and "gündüz" == "gündüz")

#not
print(not "Python" == "Python" or 2>1)
print(not "Ders" == "Ders" or 54>=87)
print(not "kurs" != "ders" and 2<5)

print(not "kurs" != "ders" or 2<5 or 99<54 and "gündüz" == "gündüz")
print(not ("kurs" != "ders" or 2<5 or 99<54 and "gündüz" == "gündüz"))
print(not ("kurs" != "ders" or 2<5 or (99<54 and "gündüz" == "gündüz")))

