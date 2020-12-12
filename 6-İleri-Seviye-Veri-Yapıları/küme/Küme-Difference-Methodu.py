
a = {1,2,3,4}
b = {2,4,5,6,7}
print(a.difference(b))

#birden fadzla kümenin elemanları arasında farkı bulur
#bir kümede olup diğer kümede olmayanları bulur

########################################################################

a = {1,2,3,4}
b = {2,4,5,6,7}
a.difference_update(b)
print(a)
print(b)

#iki küme arasında farkı bulur ve bulduğu değeri kümeye atayarak
#kümenin elemanlarını güneceller
