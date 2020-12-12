
# Programcı Hatası(eror)

#yazım yanlışı(syntax)
print('mehaba)

#yazım yanlışı(syntax)
print'merhaba

#ZeroDivisionError:bir sayı sıfıra bölünemez
print(85/0)

#ValueError:veri tipi ile tanımlanmak istenen değer uyumlu değil
int("mehaba")


#Programcı Hatası veya Mantık Hatası(bug)

#dikdörtgen alanı heseplama
uzun_kenar = int(input("uzun kenarı giriniz : "))
kısa_kenar = int(input("kısa kenari giriniz : "))
alan = 2*uzun_kenar*kısa_kenar
print(alan)
# alan uzun kenar * kısa kenar olması gerekirken biz 2 ile çarparak 
#mantık hatası yaptık


#İstisnalar
sayı1 = int(input("sayı giriniz : "))
sayı2 = int(input("sayı giriniz : "))
bölme = sayı1/sayı2
print(bölme)
#eğer ikinci sayıyı sıfır girersek ZeroDivisionError hatası alırız.
