
liste = [1,2,3,4,5]

def çarp(sayı):
	return sayı*2

map1 = map(çarp,liste)
print(map1)

############################################################

liste = [1,2,3,4,5]

def çarp(sayı):
	return sayı*2

map1 = map(çarp,liste)
print(list(map1))

###############################################################

def çarp(sayı):
	return sayı*2
list(map(çarp,[1,2,3,4,5]))

#################################################################

liste = [1,2,3,4,5]

map2 = map(lambda sayı:sayı*2,liste)
print(list(map2))

#################################################################

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]

list(map(lambda x,y:x*y,liste1,liste2))

#####################################################################

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = [7,8,9]

list(map(lambda x,y,z:x*y*z,liste1,liste2,liste3))
