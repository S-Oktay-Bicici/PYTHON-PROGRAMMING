def IPkontrol(adres):
    try:
        bolumler = adres.split('.')
        gecerli = 0

        for b in bolumler:
            if int(b)>=0 and int(b)<=255:
                gecerli += 1
        if gecerli == 4:
            return True
        else:
            return False
    except:
        return False

for n in range(4):
    a = input("IP adresi giriniz: ")
    if IPkontrol(a):
        print(a,"geçerli bir IP adresidir.")
    else:
        print(a,"geçersiz bir IP aderesidir.")