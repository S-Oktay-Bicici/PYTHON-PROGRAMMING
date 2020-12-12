#fibonacci serisinde her sayı, kendisinden önce gelen iki sayının toplamıdır.
# 4 milyondan küçük tüm çift sayıların toplamı ?

fibo = [1,2]

n = 2
toplam = 0
while fibo[n-1]<4000000:
    fibo.append(fibo[n-2]+fibo[n-1])
    if fibo[n-1]%2==0:
        toplam += fibo[n-1]
    n += 1

print(toplam)