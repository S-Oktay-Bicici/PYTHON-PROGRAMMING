
from functools import reduce

liste = [1,2,3,4,5]
reduce1 = reduce(lambda x,y:x*y,liste)
print(reduce1)
"""
1*2=2
2*3=6
6*4=24
24*5=120
"""
##############################################################

liste = [1,2,3,4,5]
reduce1 = reduce(lambda x,y:x+y,liste)
print(reduce1)
"""
1+2=3
3+3=6
6+4=10
10+5=15
"""
##################################################################

liste = [1,2,3,4,5]
print(max(liste))


liste["ahmet","ali","zehra"]
print(max(liste))
