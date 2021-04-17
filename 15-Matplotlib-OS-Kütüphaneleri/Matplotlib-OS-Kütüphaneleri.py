# %% matplotlib

import matplotlib.pyplot as plt
# kütüphaneyi ekliyoruz 
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])
# numpy kütüphanesini kullanarak 2 tane dizi oluşturuyoruz 

plt.figure()
plt.plot(x,y, color="red",alpha = 0.7, label = "line")
#rengini- saydamlığını belirtiyoeuz
plt.scatter(x,y,color = "blue",alpha= 0.4, label = "scatter")
plt.title("Matplotlib") # isism veriyoruz 
plt.xlabel("x") # eksenleri belirtiyoruz
plt.ylabel("y")
plt.grid(True) #Gridlere bölüyoruz
plt.xticks([0,1,2,3,4,5]) # kordinat sistami genişliğni belirliyoruz
plt.legend()
plt.show() # oluşturduğumuz figure yi kapatıyoruz

fig, axes = plt.subplots(2,1, figsize=(9,7))
fig.subplots_adjust(hspace = 0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]


axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(y,x)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x") 

# 2 figür çizdirdik 

# random resim oluşturuduk
plt.figure()
img = np.random.random((50,50))
plt.imshow(img, cmap = "gray") # 0(siyah) 1(beyaz) -> 0.5(gri) 
plt.show()

# %% OS

import os

print(os.name) # bulunan bilgisayar ismini döndürür 

currentDir = os.getcwd() # bulunduğumuz konumu gösterir 
print(currentDir)

# new folder
folder_name = "new_folder" # yeni bir dosya olşturma işlemi
os.mkdir(folder_name)

new_folder_name = "new_folder_2" # oluşturduğumuz dosya ismini değiştiriyoruz 
os.rename(folder_name, new_folder_name)

os.chdir(currentDir+"\\"+new_folder_name) # oluşturduğumuz dosya içerisine giriyoruz 
print(os.getcwd())

os.chdir(currentDir)
print(os.getcwd())

files = os.listdir()

for f in files:
    if f.endswith(".py"): # sadece .py ile biten dosyaları seçiyoruz 
        print(f)

os.rmdir(new_folder_name) # oluşturduğumuz dosyayı siliyoruz 

for i in os.walk(currentDir):
    print(i)  

os.path.exists("python_hatırlatma.py") # aradığımız dosya var mı kontrol ediyoruz 
