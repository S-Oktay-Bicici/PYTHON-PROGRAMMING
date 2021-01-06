# -*- coding: utf-8 -*-

import numpy as np

m = np.array([[1,2],[3,4]])
n = np.array([[6,7],[8,9]])

v = np.array([5,7])
z = np.array([8,9])

########### toplama ####################

print(np.add(n,m)) # toplama işlemi
# print(n + m) olarak da yapılabilir

print(m + 5) # bir tam sayı ile toplam işlemi
#print(np.add(m,5)) olarak da yapılabilir

print(np.add(m,v)) # matris ile vektör toplaması
#print(m + v)

############## çıkarma ################  

print(np.subtract(m,2))

####### çarpma ###################

print(np.multiply(m,4))

############# bölme #########
 
print(np.divide(n,2))

######## karekök ######

print(np.sqrt(z))

###### sum metodu ##########

# [1,2]
# [3,4]

print(np.sum(m)) # tüm elemanların toplamını verir
print(np.sum(m, axis = 0)) # y ekseni boyunca toplar 
print(np.sum(m, axis = 1)) # x ekseni boyunca toplar

#### matris çarpımı ################

print(np.dot(m,n))
# m.dot(n) olarak da yapılabirli

###### matrsi transpozu alma ############

print(m.transpose())
#print(np.transpose(m))
#print(m,T) olrakda kullanılabilir

######### array da loop ile dolaşma ######################

mat = np.array([[1,2],[3,4],[5,6]])

for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        print(mat[i,j])

####### kuyruk oluşturma ################

# sadece yan yana tile(arr,(x))

print(np.tile(mat,(2))
     
# hem yan yana hem alt alta ise tile (arr, (x,y))

print(np.tile(mat,(3,3)))


####reshape #############

arrr = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

print(np.reshape(arrr,(4,3)))

###### max ve min ###########################

print(arrr.max())
print(arrr.min())