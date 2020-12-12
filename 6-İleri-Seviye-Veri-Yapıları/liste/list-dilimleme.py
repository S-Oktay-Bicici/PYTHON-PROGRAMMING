a=[1,2,3,4,5,6,7,8]
print("Listenin Soldan Başlanarak Dilimlenmesi",a)
for i in range(0,len(a)+1):
    print("<",a[0:i], ">",sep="")
print("----------------------------------")
print("",a)
for i in range(0,len(a)+1):
    print("<",a[i:len(a)+1], ">",sep="")

    """
    Lst= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print(Lst) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print(Lst[0:3]) # [10, 20, 30]
print(Lst[4:8]) # [50, 60, 70, 80]
print(Lst[2:5]) # [30, 40, 50]
print(Lst[-5:-3]) # [80, 90]
print(Lst[:3]) # [10, 20, 30]
print(Lst[4:]) # [50, 60, 70, 80, 90, 100, 110, 120]
print(Lst[:]) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print(Lst[-100:3]) # [10, 20, 30]
print(Lst[4:100]) # [50, 60, 70, 80, 90, 100, 110, 120]
print(Lst[2:-2:2]) # [30, 50, 70, 90]
print(Lst[::]) # [10, 30, 50, 70, 90, 110]
print(Lst[::-1]) # [120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(Lst[::-2])

"""

"""
lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:5]=["a", "b", "c"] #[30, 40, 50] değerleri ["a", "b", "c"] değerleri ile değiştiriliyor
print(lst)
print("-------------------")
lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:6]=["a","b"] #[30, 40, 50, 60] değerleri ["a", "b"] değerleri ile değiştiriliyor
print(lst)
print("-------------------")
lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:2]=["a", "b", "c"] # 2 nolu indexten başlayarak ["a", "b", "c"] değerleri ekleniyor
print(lst)
print("-------------------")
lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:5]=[] # [30, 40, 50] değerleri yerine [] atanıyor. (değerler siliniyor)
print(lst)

"""