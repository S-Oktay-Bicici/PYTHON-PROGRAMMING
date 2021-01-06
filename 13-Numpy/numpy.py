import numpy as np 

python_list = [0,1,2,3,4,5,6,7,8,9] #python da list kullanım örneği
numpy_array = np.array([0,1,2,3,4,5,6,7,8,9])

print("python listesi: ",python_list)
print("numpy array:    ",numpy_array)

numpy_array2 = np.array([[0,1,2,3,4,5,6,7,8,9]]) #iki boyutlu array
print(numpy_array2)

print(numpy_array.shape)
print(numpy_array2.shape)#satır sütün değerlerini öğreniyoruz

print(numpy_array.reshape(5,2)) # iki boyutlu hale getirdik kalıcı değil
print(numpy_array2.reshape(10,)) # tek boyurlu hale getrdik kalıcı değil

numpy_array = numpy_array.reshape(5,2) # kalıcı olarak iki boyutlu hale getrdik