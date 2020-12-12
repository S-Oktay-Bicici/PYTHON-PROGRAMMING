veri = input("İşleminiz: ")
hesap = eval(veri)
print(hesap)

#eval() fonksiyonu kullanıcıya rastgele python komutları .alıştırma imkanı 
#sunmaktadır.

#eval() fonkisyonu güvenlik açısından sıkıntılı bir durum arz ettiği için 
#kullanımına dikkat edilmesi gerekir

exec("a = 45")
print(a)

#exec() fonksiyonu yardımıyla, karakter dizileri içindeki çok kapsamlı python #kodlarını işletebilirsiniz 
