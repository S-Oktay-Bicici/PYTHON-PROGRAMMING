from math import sqrt

# Kullanıcıdan değer alınıyor
sayi = float(input("Sayı Giriniz: "))
# Karakök hesaplanarak kok değişkenine aktarılıyor
kok = sqrt(sayi) # kok değişkenine sqrt fonksiyonunun sonucu aktarılmış
print(sqrt(sayi))
# Sonuçlar yazdırılıyor
print(sayi," sayısının karekökü" "=", kok)


##################################################################################
"""
# Bu program sqrt() fonksiyonunun farklı kullanımlarını gösterir.
x = 16
# İstenilen sabit değerin karekökünün alınması
print("1 = >",sqrt(16.0))
# Değişkenin karekökünün alınmasını sağlar
print("2 = >",sqrt(x))
# sqrt() fonksiyonunun içerisinde işlem kullanımı
print("3 = >",sqrt(2 * x - 5))
# İşlem sonucu geri dönen değerin değişkene aktarılması
y = sqrt(x)
print("4 = >",y)
# İçerisinde işlem kullanılan sqrt() fonksiyonunun dönen değerinin işleme tabi tutulması
y = 2 * sqrt(x + 16) - 4
print("5 = >",y)
# İç içe sqrt() fonksiyonunun kullanılması
y = sqrt(sqrt(256.0))
print("6 = >",y)
print("7 = >",sqrt(int("45")))

"""

#########################################################################
"""
x = 2
print("x = 2....",x)
print("sqrt(x).....",sqrt(x))
print("x.....",x)
x = sqrt(x)
print("x = sqrt(x) .....x => ",x)

"""