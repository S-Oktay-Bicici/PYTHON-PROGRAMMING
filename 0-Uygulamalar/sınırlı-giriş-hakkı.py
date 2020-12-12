# ### Bir kullanıcı adı ve parola belirleyin. Kullanıcıya kullanıcı adını ve parolasını sorun. Eğer ikisi de doğruysa kullanıcı giriş yapabilsin. Değilse giriş yapamasın. 3 Giriş Hakkı olsun

username = "Python"
password = "Monty123"

kalan_hak = 3

while kalan_hak > 0:
    uname = input("Kullanıcı adınız: ")
    pw = input("Parolanızı giriniz: ")
    
    if username == uname and password == pw:
        print("Giriş Başarılı, Hoşgeldiniz", username)
        break
    
    else:
        kalan_hak = kalan_hak - 1
        print("Giriş Başarısız. Kalan Hakkınız:", kalan_hak)

if kalan_hak == 0:
    print("Şifreniz bloke oldu.")

