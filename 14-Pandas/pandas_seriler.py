# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd 

#seriler=pd.Series(data,index)
#data=sabit bir değer,liste,numpy dizisi,dictionary(sözlük)

sayılar=[0,1,2,3,4,5,6,7,8,9]
numpy_array=np.array(sayılar)
print(numpy_array)

seriler=pd.Series(data=sayılar)
print(seriler)

my_index=['a','b','c','d','e','f','g','h','i','j']
seriler=pd.Series(data=sayılar,index=my_index,dtype=int)
print(seriler)

sözlük={'a':0,'b':1,'c':2,'d':3}
seriler=pd.Series(data=sözlük)
print(seriler)

print(seriler.ndim) # serinin boyutunu öğrnemek için 
print(seriler.dtype) # serinin veri tipini öğrenmek için 
print(seriler.shape) # serinin stır ve sütün syısını öğrenmek için

############### matematiksel ve aritmetik fonksiyonlar ################

sayılar=[0,1,2,3,4,5,6,7,8,9]
seriler1=pd.Series(data=sayılar)

print(seriler1.sum()) # serinin toplamını verir

print(seriler1.min()) # min değerini döndürür

print(seriler1.max()) # max değerini döndürür

print(seriler1.mean()) # ortalamasnı döndürür

print(seriler1.median()) # ortancasını verir

print(seriler1.var())

print(seriler1.std()) # standar sapamayı döndürür

sayılar2=[9,8,7,6,5,4,3,2,1,0]
seriler2=pd.Series(data=sayılar2)

print(seriler1+seriler2)
print(seriler1+5)

print(seriler1-seriler2)

print(seriler1*seriler2)
print(seriler*3)

print(seriler1/seriler2)

########################################

print(seriler1[seriler1>5]) # 5 den büyük olan değerler döner

print(seriler1[seriler1>seriler1.mean()]) # ortalamasan büyük olan değerler döner

print(seriler1[seriler1==4]) # değeri 4 olan ifadeyi döner

print(seriler1[seriler1<=5]) # 5 den küçük olaün değerler döner

