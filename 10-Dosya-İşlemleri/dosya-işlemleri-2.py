# # Python'da Dosya Oluşturma, Okuma, Yazma,
# # Güncelleme ve Silme İşlemleri yapılabilir.

# # Dosya Erişimi
# 
# ### open() fonksiyonu filename ve mode parametreleri
# 
# ### 'r' --> read (Okuma)
# ### 'a' --> append (Ekleme) 
# ### 'w' --> write (Yazma)
# ### 'x' --> create (Oluşturma)
# ### Ek modlar: 't' --> text olarak veya 'b' binary olarak açmak için
# ### Örnek: open("resim.png", "rb") veya open("data.txt", "w")

# # -r read modu

file = open("deneme.txt", "r")
print(file)
file.close()


# ### read() fonksiyonu açılan dosyadaki veriyi döner
file = open("deneme.txt", "r")
print(file.read())
file.close()

###################################################################

file = open("deneme.txt", "rb")
print(file.read())
file.close()


# ### read(n) ilk n karakteri okur
file = open("deneme.txt", "r")
print(file.read(15))
file.close()


# ### readline() fonksiyonu her bir satırı birer birer okur
file = open("deneme.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


# ### for loop ile direkt olarak satırları okuyabiliriz
file = open("deneme.txt", "r")

for line in file:
    print(line)

file.close()


# ### Türkçe karakter okuyabilir miyiz?
file = open("deneme_turkish.txt", "r")
print(file.read())
file.close()

###################################################

file = open("deneme_turkish.txt", "rb")
print(file.read())
file.close()


# ### utf-8 encoding parametresi Türkçe karakter sorununu çözer
file = open("deneme_turkish.txt", "r", encoding="utf-8")
print(file.read())
file.close()


# # -a append modu

# ### write() fonksiyonu dosyaya açılan modda veriyi yazar
file = open("deneme_turkish.txt", "r", encoding="utf-8")
print(file.read())
file.close()

file = open("deneme_turkish.txt", "a", encoding="utf-8")
print(file.write("\ntürkçe metin ekledim"))
file.close()

file = open("deneme_turkish.txt", "r", encoding="utf-8")
print(file.read())
file.close()


# # -w write modu

# ### write modu, açılan dosyanın tüm içeriğini temizler ve üstüne yazar (overwrite)
file = open("deneme_turkish5.txt", "r", encoding="utf-8")
print(file.read())
file.close()


# # Yeni dosya oluşturma -x modu
# ## (-a ve -w modu da kullanılabilir )
file = open("deneme2.txt", "x", encoding="utf-8")
file.write("Merhaba")
file.close()


# # Farklı directory'lerdeki dosyalara gitme

# ### os modülü
import os


# ### os get current working directory
os.getcwd()


# ### os list directories
os.listdir("../11Python")


# ### başka bir directory'de dosya açma
file = open("../11Python/new2.txt", "w")
file.write("Merhaba bu da 3. dosya")
file.close()


# ### başka directory'lerdeki dosyaları okuma
path = "../11Python"
for filename in os.listdir(path):
    if filename.startswith("new"):
        print(path+"/"+filename)
        file = open(path+"/"+filename, "r")
        print(file.read())
        file.close()


# ### mkdir ve makedirs ile yeni directory/ler oluşturma
import os
path = "../11Python"
os.makedirs(path+ "/new_folder/new2_folder")


# # Dosyayı silme
path = "../11Python"
if os.path.exists(path+"/new2.txt"):
    os.remove(path+"/new2.txt")
else:
    print("File not found")


# # Directory silme

# ### directory silmek için, içerisinde hiç dosya olmaması gerekmektedir
os.rmdir("../11Python/Untitled Folder")


# # Dosya kopyalama
file = open("../11Python/new3.txt", "rb")
binaries = file.read()
file.close()

file2 = open("new(copy).txt", "wb")
file2.write(binaries)
file2.close()


# # Dosya taşıma
file = open("../11Python/new3.txt", "rb")
binaries = file.read()
file.close()

file2 = open("new(moved).txt", "wb")
file2.write(binaries)
file2.close()

os.remove("../11Python/new3.txt")


