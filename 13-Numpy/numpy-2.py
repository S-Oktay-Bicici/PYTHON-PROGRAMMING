# -*- coding: utf-8 -*-

import numpy as np

a = np.array([[1,2,3],[4,5,6]])

print(a)
print(a.dtype) #matrisin veri tipini öğreniyoruz

a = np.array([[1,2,3],[4,5,6]], dtype = np.float64)# zorla tip ataması gerçekleştirdik
print(a)


liste = [[1,"b",3],["s",5,6]]
o = np.array(liste)
print(o)
print(o.dtype)

######### KISA YOLDAN MATRİS OLUŞTURMA ###################

# np.zeros((a,b)) --> a X b boyutunda tamamı 0 lardan oluşan bir matris oluşturur
# np.ones((a,b)) --> a X b boyutunda tamamı 1 lerden oluşan bir matris oluşturur
# np.full((a,b),n) --> a X b boyutunda tamamı n lerden oluşan bir matris oluşturur
# np.eye(a) --> a X a boyutunda bir ıdentity matrisi oluşturur (köşegenler 1, diğerleri 0)
# np.random.random((a,b)) --> a X b boyutunda tamamı [0-1] arasındaki random sayılardan oluşan bir matris oluşturur

n = np.full((4,4),3)
print(n)

print(np.zeros_like(n)) # n array yapısına benzeyen zeros bir array oluşturuyor

########## Matris elemanlarına elişim ##############

lst = [[1,2,3,4,5],[0,9,8,7,6],[3,5,7,9,11],[2,4,6,8,10]]

arr = np.array(lst)
print(arr[1:3,1:])
print(arr[:,2:4])

arr[0,2] = 13 # değer değişikliği yapabiliyoruz
print(arr[0,2])

arr[1,2:] = [28,27,26] #çoklu değer değişikliği yapılabilr
arr[2,2:] = 1

print(arr[1])
print(arr[2])

print(arr)
print(arr[np.arange(3), np.arange(1,4)])
print(arr[np.arange(3), np.arange(1,4)]) *= 5
print(arr)
