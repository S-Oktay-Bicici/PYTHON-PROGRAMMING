def yuzler():
    num = 100
    while num<1000:
        yield num
        num += 100

for deger in yuzler():
    print(deger)