
#ZeroDivisionError
num1 = 7
num2 = 0
print(num1/num2)

############################################
try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("işlem tamam")
except ZeroDivisionError:
    print("sıfıra bölüm hatası")

###########################################

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("sıfıra bölüm hatsı")
except (ValueError, TypeError):
    print("değer yada tip hatası")

###################################################

try:
    print("hello")
    print(1/0)
except ZeroDivisionError:
    print("sıfıra bölüm")
finally:
    print("burdaki kod mutlaka çalışır")

####################################################

try:
    print("hello")
    print(1/0)
except ZeroDivisionError:
    print("sıfıra bölüm")
else:
    print("burdaki kod mutlaka çalışır")

#####################################################

try:
    print("hello")
    print(1/0)
except ZeroDivisionError:
    print("sıfıra bölüm")
else:
    print("no error")
finally:
    print("daima finally bloğu çalışır")

#######################################################

#hata oluşturma raise

sayi = input("Pozitif sayi gir:")
if float(sayi)<0:
    raise ValueError("Negative!!!")