
def faktoriyel(n):
	print("Çağrılan faktoriyel sayısı n : " + str(n))
	if n == 1:
		return 1
	else:
		sonuç = n * faktoriyel(n-1)
		print("Öneceki işlem sonucu : ",n, "faktoriyel (" ,n-1, ") : ",sonuç)
		return sonuç

print(faktoriyel(5))
