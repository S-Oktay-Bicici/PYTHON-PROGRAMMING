# -*- coding: utf-8 -*-

import pandas as pd 

df = pd.read_csv("covid_19_data.csv")
print(df)

print(df.shape) # satır sütün sayılarını elde ediyoruz

print(df.columns) # sütünları döndürür

print(df.dtypes) #sütünların data tiplerini dönüdürür

print(df.head(10)) # ilk 10 değere ulaşırız

print(df.tail(10)) # en son 10 değere ulaşırız

print(df.info()) 

print(df.isnull().sum()) # boş bırakılan kısımların toplamını döndürür

print(df.describe()) # sütünların istatistiksel özelliğini döndürür

print(df["Province/State"].describe()) # belirtiğimiz satırdaki string analızi gerçekleşiyor

first = df["Province/State"] # datada sadece şehir verilerini çektik 
print(first)

second = df[["Province/State","Country/Region"]] # datada hem şehir hem ülke verileri çekltik 
print(second)

#loc(satır,sutun)
c1 = df.loc[1]
print(c1)

c2 = df.loc[1:55] # 1. satırdaki ilk 55 sutun alınır 55 dahil
print(c2)

c3 = df.loc[:,"Province/State"] # şehirler sutununfan tüm satıraları alıyoruz
print(c3)

c4 = df.loc[:,["Province/State","Country/Region"]] # şehir ve ülke sutununfan tüm satırları alıyoruz
print(c4)

c5 = df.loc[3:45,["Province/State","Country/Region"]] # şehir ve ülke sutununfan 3 ile 45 arasındaki yüm satırları aldı
print(c5)

c6 = df.iloc[5] #5. indeksteki değerlere ulaşırım
print(c6)

c7 = df[df.Deaths<10] # ölüm sayısı 10 dan küçük ölüm sayılarını çağırır
print(c7)

#############################################################################

a1=df.sort_values(by='Deaths',ascending=False).head(20)# azalan şeklde ölü listesini alıyoruz
print(a1)

df=df.drop(12969) # indeksi verilen değeri siliyoruz
print(df.sort_values(by='Deaths',ascending=False).head(20))  

df.drop(12649,inplace=True) # indeksi verilen değeri siliyoruz
print(df.sort_values(by='Deaths',ascending=False).head(20))


"""
df=df.drop("SNo",axis=1) # verilen sutunu siliyoruz
print(df.sort_values(by='Deaths',ascending=False).head(20))
"""
df=df.drop(columns="SNo") # verilen sutunu siliyoruz
print(df.columns)

print(df.groupby("Province/State")["Deaths"].mean().head(10))# verilen iki sutuun ortalama ilk 10 değeri getirir
print(df.groupby("Province/State")["Deaths"].max().head(10)) # veriln iki sutunda max 10 değeri getiri
print(df.groupby(["Province/State","Country/Region"])["Deaths"].max().head(10))


print(df.isnull().sum()) # non değerleri buluypruz

df["Province/State"].fillna(method="ffill",inplace=True) # boş satırı kendinden önceki değeri yazdırarak boşlukları bitirir

print(df.isnull().sum())

#df=df.drop() 