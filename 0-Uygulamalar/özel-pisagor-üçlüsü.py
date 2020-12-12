bulundu = False
for a in range(30,400):
    for b in range(a+1,450):
        if a**2 + b**2 == (1000-a-b)**2:
            bulundu = True
            break
    if bulundu:
        break

print(a,b,1000-a-b)